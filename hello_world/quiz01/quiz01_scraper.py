"""First selenium script.

Returns:
    _type_: _description_
"""
# import argparse
import configparser
import logging
import os
import uuid
from typing import List  # , Optional

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from swagger_client import QuestionModel

from . import config
from .quiz01_api import Quiz01Service, Quiz01ServiceFromClient
from .quiz01_util import log_method_call

STR_TOFC = 'True or False:'
STR_TOFCS = 'True or False: '
STR_NOT = 'NOT'
RADIO = 'RADIO'
CHECK = 'CHECK'
RADIO_BOOL = 'RADIO_BOOL'
EW = 20  # EW stands for explicit_wait
XPATH_1ST_BTN = (
    '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button')
XPATH_2ND_BTN = (
    '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button[2]')
XPATH_ANSW_Q_DIV = (
    '/html/body/'
    'div/ion-app/div/div[1]/ion-content/div/div[2]/div/div[4]/div/'
    'ion-card/ion-card-content/div/ion-list/ion-list-header/div/div')
XPATH_ANSW_Q_CHEK_RADI = (
    '//*[starts-with(@id, "question-")]/ion-card/ion-card-content/div/'
    'ion-list/ion-item'
    ' | '
    '//*[starts-with(@id, "question-")]/ion-card/ion-card-content/div/'
    'ion-list/ion-radio-group/ion-item')


class EnvInterpolation(configparser.BasicInterpolation):
    """Interpolation which expands environment variables in values."""
    # https://stackoverflow.com/questions/26586801/configparser-and-string-interpolation-with-env-variable

    def before_get(self, parser, section, option, value, defaults):
        """Funcion de sobreEscritura."""
        value = super().before_get(parser, section, option, value, defaults)
        return os.path.expandvars(value)


ini = configparser.ConfigParser(interpolation=EnvInterpolation())
# config = configparser.ConfigParser()
# config = configparser.ConfigParser(os.environ)
# config = configparser.ConfigParser(
#     os.environ,
#     interpolation=configparser.ExtendedInterpolation())
# config = configparser.SafeConfigParser(os.environ)
ini.read('config.ini')


def _click(driver, xpath: str):
    WebDriverWait(driver, EW).until(EC.element_to_be_clickable(
        (By.XPATH, xpath))).click()


def _analyze_feedback_question(feedback) -> tuple:  # tuple[str, str]:
    """Determinar el tipo de pregunta."""
    str_input_type = ''
    str_question = ''

    try:
        str_question = (
            feedback.
            contents[0].contents[0].next_sibling.
            contents[0].contents[0].contents[0].
            contents[0].contents[0].next_element.text)
        str_input_type = RADIO
    except Exception as e1:
        logging.warning(str(e1), exc_info=True)

        try:
            # we_question stands for WebElement Question
            we_question = (
                feedback.
                contents[0].contents[0].next_sibling.div.
                contents[0].contents[0].contents[0].contents[0].contents[0].
                next_element)
            str_input_type = CHECK

            if we_question.text == STR_TOFC:
                str_input_type = RADIO_BOOL
                str_question = we_question.next_element.text.lstrip()

            elif we_question.text[-1] == ' ':
                if we_question.next_element.next_element.text == STR_NOT:
                    str_question = (
                        we_question.text +
                        we_question.next_element.next_element.text +
                        we_question.next_element.next_element.next_element.
                        text)
            else:
                str_question = we_question.text

        except Exception as e2:
            logging.error(str(e2), exc_info=True)

    return str_input_type, str_question.strip().replace('\xa0', ' ')  # FIXED


def _mark_dom_answers(driver, scrapped_answers_to_choose):
    for scrapped_answer in scrapped_answers_to_choose:
        _roll_n_click_to_answer(driver, scrapped_answer)


def _roll_n_click_to_answer(driver, scrapped_answer):
    driver.execute_script(
        "arguments[0].scrollIntoView(true);", scrapped_answer)
    # browser.execute_script("arguments[0].click();", answer)
    # answer.click()
    WebDriverWait(driver, EW).until(
        EC.element_to_be_clickable(scrapped_answer)).click()


def _process_feeback_ticks(
        p_ticks,
        p_exam_number: int,
        p_question_text,
        p_type,
        p_flag_correct,
        p_obj_service: Quiz01Service,
        p_flag_dont_override=False,
        p_flag_batch: bool = False,
        p_lista_put: List[QuestionModel] = []):
    for tick in p_ticks:
        if p_type == RADIO_BOOL:
            f_answer_ok_text = (
                tick.previous_sibling.next_element.next_element.
                next_element.next_element.next_element.text)
        else:
            f_answer_ok_text = (
                tick.previous_sibling.next_element.next_element.
                next_element.next_element.next_element.next_element.text)

        f_answer_ok_text = f_answer_ok_text.strip()  # FIXED
        print(f_answer_ok_text)
        logging.info(f_answer_ok_text)
        if p_flag_batch:
            if p_flag_dont_override:
                stored_data = p_obj_service.get_cache(exam_number)
                filtered_data = list(filter(
                    lambda i:
                        i['id'] == p_question_text and
                        i['question_type'] == p_type and
                        i['answer_text'] == f_answer_ok_text and
                        i['is_correct'] == p_flag_correct and
                        i['exam_number'] == p_exam_number,
                        stored_data['Items']))

                if filtered_data:
                    continue

            p_lista_put.append(
                QuestionModel(
                    id=p_question_text,
                    question_type=p_type,
                    answer_text=f_answer_ok_text,
                    is_correct=p_flag_correct,
                    exam_number=p_exam_number,
                    last_modified=config.currentDT.isoformat()))
        else:
            p_obj_service.put(
                f'{p_question_text}---{f_answer_ok_text}',
                p_question_text, p_type, f_answer_ok_text,
                p_flag_correct, p_exam_number, config.currentDT.isoformat())


@log_method_call
def do_scraping(p_exam_number: int):
    """Main method."""
    global exam_number
    exam_number = p_exam_number
    exam_section = f'EXAM-{exam_number}'
    quiz_url = ini[exam_section]['quiz_url']
    x_api_key = ini[exam_section]['x-api-key']
    api_put = ini[exam_section]['api_put']
    api_search = ini[exam_section]['api_search']
    api_endpoint = ini[exam_section]['api_endpoint']
    obj_service: Quiz01Service = Quiz01ServiceFromClient(
        x_api_key,
        api_endpoint
    )

    v_uuid = uuid.uuid4().hex
    print(f'v_uuid->{v_uuid}')
    logging.info(f'v_uuid->{v_uuid}')

    driver_location = ini['DEFAULT']['driver_location']
    binary_location = ini['DEFAULT']['binary_location']
    headless = ini.getboolean('DEFAULT', 'headless')
    do_correct_answers = ini.getboolean('DEFAULT', 'do_correct_answers')
    do_correct_answers_cache = ini.getboolean(
        'DEFAULT', 'do_correct_answers_cache')
    dont_override = ini.getboolean('DEFAULT', 'dont_override')
    dont_store_answers = ini.getboolean('DEFAULT', 'dont_store_answers')

    options = Options()
    options.binary_location = binary_location
    # ua = UserAgent()
    # userAgent = ua.random
    # log.info(userAgent)
    # opts_chrome.add_argument(f'user-agent={userAgent}')
    # opts_chrome.add_argument(
    #     'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    #     'AppleWebKit/537.36 (KHTML, like Gecko) '
    #     'Chrome/80.0.3987.149 Safari/537.36')
    if headless:
        options.add_argument("--headless")
        # options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--no-sandbox')
    else:
        options.add_argument("--start-fullscreen")  # or with --
    # options.add_argument("start-maximized")
    options.add_argument("--incognito")  # or without --

    # not working on latest versions of driver
    # options.add_argument("--disable-infobars")
    # options.add_argument("--disable-extensions")
    options.add_argument("allow-insecure-localhost")
    options.add_argument("ignore-ssl-errors=yes")
    options.add_argument("ignore-certificate-errors")
    options.add_argument("--log-level=3")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    service = Service(driver_location)
    # Create new Instance of Navigator
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(quiz_url)

    # page_source = driver.page_source

    # codigo para probar si tenemos lxml antes de empezar
    # soup = BeautifulSoup(page_source, 'lxml')

    # don't activate this cause will interfere with WebDriverWait
    # default is zero
    # driver.implicitly_wait(implicitly_wait)

    _click(driver, XPATH_1ST_BTN)  # press 1st button Next
    _click(driver, XPATH_2ND_BTN)  # press 2nd button Next

    logging.info('SECTION - ANSWERING QUESTIONS')
    while True:
        try:
            WebDriverWait(driver, 3).until_not(
                EC.visibility_of_element_located((By.XPATH, XPATH_ANSW_Q_DIV)))
        except Exception as ex1:
            logging.error(str(ex1), exc_info=True)
        finally:
            div_question_text = WebDriverWait(driver, EW).until(
                EC.visibility_of_element_located((By.XPATH, XPATH_ANSW_Q_DIV)
                                                 )).text.split("\n")[0]
            if div_question_text.startswith(STR_TOFCS):
                div_question_text = div_question_text.split(STR_TOFCS)[1]

            div_question_text = div_question_text.strip().replace('\xa0', ' ')  # FIXED
            print(div_question_text)

        # WebDriverWait(driver, ew).until(EC.invisibility_of_element_located(
            # (By.XPATH, XPATH_ANSW_Q_DIV)))
        # div_question = WebDriverWait(driver, ew).until(
            # EC.presence_of_element_located((By.XPATH, XPATH_ANSW_Q_DIV)))
        # print(div_question.text)

        # SECTION - ANSWERING QUESTIONS - CHECKBOXES or RADIO BUTTONS
        scraped_answers_to_choose = driver.find_elements(
            By.XPATH, XPATH_ANSW_Q_CHEK_RADI)

        if not do_correct_answers:
            logging.info('SECTION - DUMMY ANSWERS')
            _mark_dom_answers(driver, scraped_answers_to_choose)
        elif do_correct_answers and do_correct_answers_cache:
            logging.info('SECTION - DO CORRECT ANSWERS - CACHE')
            stored_data = obj_service.get_cache(exam_number)
            filtered_data = list(filter(
                lambda i:
                i['id'] == div_question_text and
                i['is_correct'],
                stored_data['Items']))

            # DONE | IMPROVE THIS BUCLE | YA NO
            # 1 -> the stored answers COULd be the 2 last of the list
            # 2 -> the stored answer could be non existant
            if filtered_data:
                logging.info('ITEM - DATA FOUND')
                for stored_item in filtered_data:
                    for scraped_answer in scraped_answers_to_choose:
                        scraped_answer_txt = scraped_answer.find_element(
                            By.CLASS_NAME, 'bbcode, cursor-pointer').text
                        if (stored_item['answer_text'] == scraped_answer_txt):
                            _roll_n_click_to_answer(driver, scraped_answer)
                            break
            else:
                logging.info('ITEM - DATA NOT FOUND - DUMMY ANSWERS')
                _mark_dom_answers(driver, scraped_answers_to_choose)
        elif do_correct_answers:
            logging.info('SECTION - DO CORRECT ANSWERS')
            stored_data = obj_service.search_v2(
                question=div_question_text, flag_correct=True)
            if stored_data['Items']:
                logging.info('ITEM - DATA FOUND')
                for stored_item in stored_data['Items']:
                    for scraped_answer in scraped_answers_to_choose:
                        scraped_answer_txt = scraped_answer.find_element(
                            By.CLASS_NAME, 'bbcode, cursor-pointer').text
                        if stored_item['answer'] == scraped_answer_txt:
                            _roll_n_click_to_answer(driver, scraped_answer)
                            break
            else:
                logging.info('ITEM - DATA NOT FOUND - DUMMY ANSWERS')
                _mark_dom_answers(driver, scraped_answers_to_choose)

        btn_css_selector = (
            'ion-button[data-cy="continue-btn"]'
            ','
            'ion-button[data-cy="finish-btn"]')
        WebDriverWait(driver, EW).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, btn_css_selector)))
        btn_next_or_finish_now = driver.find_element(
            By.CSS_SELECTOR, btn_css_selector)

        attribute_data_cy = btn_next_or_finish_now.get_attribute('data-cy')

        if attribute_data_cy == 'continue-btn':
            btn_next_or_finish_now.click()
            # WebDriverWait(driver, ew).until(EC.element_to_be_clickable(
            #   btn_next_or_finish_now)).click()

            # Este se encarga de waitear a la pregunta,
            # de arriba que es donde se cae
            # time.sleep(2)
        elif attribute_data_cy == 'finish-btn':
            # seccion del boton "Confirm finish"
            # time.sleep(2)
            btn_next_or_finish_now.click()
            # WebDriverWait(driver, ew).until(EC.element_to_be_clickable(
            #   btn_next_or_finish_now)).click()
            # time.sleep(2)
            # seccion del boton "Confirm finish now"
            # btn_confirm_finish_now = driver.find_element(
            #   By.XPATH, '//*[@id="test_confirm_finish"]')
            # btn_confirm_finish_now.click()
            WebDriverWait(driver, EW).until(
                EC.element_to_be_clickable((
                    By.XPATH, '//*[@id="test_confirm_finish"]')
                )).click()
            break

    logging.info(
        'HACER UN WAIT DE LA PAGINA DE RESULTADO, '
        'DEL LA PARTE DE ARRIBA Y LA DE ABAJO DE LA PAGINA')

    # WebDriverWait(driver, ew).until(EC.element_to_be_clickable(
    #   (By.XPATH, '//*[@id="logo-area"]/div/div/img')))
    WebDriverWait(driver, EW).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="contents"]/ion-card[1]')))
    WebDriverWait(driver, EW).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="contents"]/ion-card[2]')))
    WebDriverWait(driver, EW).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="contents"]/div')))

    logging.info('SCANNING CORRECT ANSWERS FROM FEEDBACK PAGE')

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    contador_preguntas = 0
    feedbacks = soup.find_all('div', class_='feedback')

    lista_put: List[QuestionModel] = []
    for feedback in feedbacks:
        contador_preguntas += 1
        print(feedback.text)

        f_type, f_question_text = _analyze_feedback_question(feedback)

        print(f'Q{contador_preguntas} - {f_question_text}')
        logging.info(f'Q{contador_preguntas} - {f_question_text}')

        correct_ticks = feedback.select(
            '.circular-tick,.circular-tick-holo')
        _process_feeback_ticks(
            correct_ticks,
            exam_number,
            f_question_text,
            f_type,
            True,
            obj_service,
            dont_override,
            True,
            lista_put)

        incorrect_ticks = feedback.select(
            'ion-icon.icon.icon-correct.md.hydrated'
            ':not(.circular-tick-holo)'
            ':not(.circular-tick)')
        _process_feeback_ticks(
            incorrect_ticks,
            exam_number,
            f_question_text,
            f_type,
            False,
            obj_service,
            dont_override,
            True,
            lista_put)

        print(f'Q{contador_preguntas} - END')
        logging.info(f'Q{contador_preguntas} - END')

    print(f'ITEMS ({len(lista_put)}) READY TO BATCH')

    if dont_store_answers:
        print('ITEMS ARE NOT GONNA BE BATCH')

    if lista_put and not dont_store_answers:
        print('BATCHING ITEMS')
        obj_service.put_batch(lista_put)
    else:
        print('ITEMS WERE NOT BATCHED')

    driver.quit()
