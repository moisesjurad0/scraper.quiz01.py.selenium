"""First selenium script.

Returns:
    _type_: _description_
"""
import argparse
import configparser
import os
import datetime
import logging
import sys
import uuid
from pathlib import Path

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import quiz01_api

STARS_SEPARATOR = '***************'
STR_TOFC = 'True or False:'
STR_TOFCS = 'True or False: '
RADIO = 'RADIO'
CHECK = 'CHECK'
RADIO_BOOL = 'RADIO_BOOL'
EW = 20  # EW stands for explicit_wait
script_path = Path(__file__).absolute()
script_dir = Path(__file__).parent.absolute()
log_folder = script_dir / 'logs'
log_folder.mkdir(parents=True, exist_ok=True)

currentDT = datetime.datetime.now()

logging.basicConfig(
    filename=log_folder / f'scrap01{currentDT.strftime("%Y%m%d%H%M%S")}.log',
    level=logging.INFO,
    format=('%(asctime)s | %(name)s | %(levelname)s |'
            ' [%(filename)s:%(lineno)d] | %(message)s'))

logger = logging.getLogger('scrapping01')
logger.setLevel(logging.INFO)
logger.info('inicio')

# https://stackoverflow.com/questions/26586801/configparser-and-string-interpolation-with-env-variable


class EnvInterpolation(configparser.BasicInterpolation):
    """Interpolation which expands environment variables in values."""

    def before_get(self, parser, section, option, value, defaults):
        """Funcion de sobreEscritura."""
        value = super().before_get(parser, section, option, value, defaults)
        return os.path.expandvars(value)


config = configparser.ConfigParser(interpolation=EnvInterpolation())
# config = configparser.ConfigParser()
# config = configparser.ConfigParser(os.environ)
# config = configparser.ConfigParser(
#     os.environ,
#     interpolation=configparser.ExtendedInterpolation())
# config = configparser.SafeConfigParser(os.environ)
config.read('config.ini')


def _analyze_feedback_question(feedback) -> set():
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
        logger.warning(str(e1), exc_info=True)

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
                if we_question.next_element.next_element.text == 'NOT':
                    str_question = (
                        we_question.text +
                        we_question.next_element.next_element.text +
                        we_question.next_element.next_element.next_element.
                        text)
            else:
                str_question = we_question.text

        except Exception as e2:
            logger.error(str(e2), exc_info=True)

    return str_input_type, str_question


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


def _process_feeback_ticks(ticks, exam_number, f_question_text,
                           f_type, flag_correct, obj_service):
    for tick in ticks:
        if f_type == RADIO_BOOL:
            f_answer_ok_text = (
                tick.previous_sibling.next_element.next_element.
                next_element.next_element.next_element.text)
        else:
            f_answer_ok_text = (
                tick.previous_sibling.next_element.next_element.
                next_element.next_element.next_element.next_element.text)
        print(f_answer_ok_text)
        logger.info(f_answer_ok_text)
        obj_service.put(
            f'{f_question_text}---{f_answer_ok_text}',
            f_question_text, f_type, f_answer_ok_text,
            flag_correct, exam_number, currentDT.isoformat())


def main():
    """Main method."""
    parser = argparse.ArgumentParser(description='Scraper0X')
    parser.add_argument(
        '-n',
        '--examnumber',
        required=False,
        help=('Parametro para decidir que examen ejecutar. '
              'Dejarlo vacio usa el default del config.ini'),
        default='1')
    args = parser.parse_args()
    logger.info(f'{STARS_SEPARATOR} PARAMETROS DE ENTRADA => '
                f'--examnumber:{args.examnumber}'
                f' {STARS_SEPARATOR}')
    exam_number = args.examnumber

    exam_section = f'EXAM-{exam_number}'
    quiz_url = config[exam_section]['quiz_url']
    x_api_key = config[exam_section]['x-api-key']
    api_put = config[exam_section]['api_put']
    api_search = config[exam_section]['api_search']

    obj_service = quiz01_api.Service(x_api_key, api_put, api_search)

    v_uuid = uuid.uuid4().hex
    print(f'v_uuid->{v_uuid}')
    logger.info(f'v_uuid->{v_uuid}')

    driver_location = config['DEFAULT']['driver_location']
    binary_location = config['DEFAULT']['binary_location']
    headless = config.getboolean('DEFAULT', 'headless')
    do_correct_answers = config.getboolean('DEFAULT', 'do_correct_answers')

    service = Service(driver_location)
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

    # Create new Instance of Navigator
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(quiz_url)

    # page_source = driver.page_source

    # codigo para probar si tenemos lxml antes de empezar
    # soup = BeautifulSoup(page_source, 'lxml')

    # don't activate this cause will interfere with WebDriverWait
    # default is zero
    # driver.implicitly_wait(implicitly_wait)

    # press 1st button Next
    WebDriverWait(driver, EW).until(EC.element_to_be_clickable(
        (By.XPATH,
         '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button')
    )).click()

    # press 2nd button Next
    WebDriverWait(driver, EW).until(EC.element_to_be_clickable(
        (By.XPATH,
         '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button'
         '[2]')
    )).click()

    logger.info('SECTION - ANSWERING QUESTIONS')
    while True:
        div_xpath = (
            '/html/body/'
            'div/ion-app/div/div[1]/ion-content/div/div[2]/div/div[4]/div/'
            'ion-card/ion-card-content/div/ion-list/ion-list-header/div/div')
        try:
            WebDriverWait(driver, 3).until_not(
                EC.visibility_of_element_located((By.XPATH, div_xpath)))
        except Exception as ex1:
            logger.error(str(ex1), exc_info=True)
        finally:
            div_question_text = WebDriverWait(driver, EW).until(
                EC.visibility_of_element_located(
                    (By.XPATH, div_xpath)
                )).text.split("\n")[0]
            if div_question_text.startswith(STR_TOFCS):
                div_question_text = div_question_text.split(STR_TOFCS)[1]
            print(div_question_text)

        # WebDriverWait(driver, ew).until(EC.invisibility_of_element_located(
            # (By.XPATH, div_xpath)))
        # div_question = WebDriverWait(driver, ew).until(
            # EC.presence_of_element_located((By.XPATH, div_xpath)))
        # print(div_question.text)

        # SECTION - ANSWERING QUESTIONS - CHECKBOXES or RADIO BUTTONS
        scrapped_answers_to_choose = driver.find_elements(
            By.XPATH,
            '//*[starts-with(@id, "question-")]/ion-card/ion-card-content/div/'
            'ion-list/ion-item'
            ' | '
            '//*[starts-with(@id, "question-")]/ion-card/ion-card-content/div/'
            'ion-list/ion-radio-group/ion-item')

        if do_correct_answers:
            logger.info('SECTION - DO CORRECT ANSWERS')
            stored_data = obj_service.search_v2(
                question=div_question_text, flag_correct=True)
            if stored_data:
                logger.info('ITEM - DATA FOUND')
                for stored_item in stored_data:
                    for scrapped_answer in scrapped_answers_to_choose:
                        scrapped_answer_txt = scrapped_answer.find_element(
                            By.CLASS_NAME, 'bbcode, cursor-pointer').text
                        if stored_item['answer'] == scrapped_answer_txt:
                            _roll_n_click_to_answer(driver, scrapped_answer)
                            break
            else:
                logger.info('ITEM - DATA NOT FOUND - DUMMY ANSWERS')
                _mark_dom_answers(driver, scrapped_answers_to_choose)

        else:
            logger.info('SECTION - DUMMY ANSWERS')
            _mark_dom_answers(driver, scrapped_answers_to_choose)

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

    logger.info(
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

    logger.info('SCANNING CORRECT ANSWERS FROM FEEDBACK PAGE')

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    contador_preguntas = 0
    feedbacks = soup.find_all('div', class_='feedback')
    for feedback in feedbacks:
        contador_preguntas += 1
        print(feedback.text)

        f_type, f_question_text = _analyze_feedback_question(feedback)

        print(f'Q{contador_preguntas} - {f_question_text}')
        logger.info(f'Q{contador_preguntas} - {f_question_text}')

        correct_ticks = feedback.select(
            '.circular-tick, .circular-tick-holo')
        _process_feeback_ticks(correct_ticks, exam_number,
                               f_question_text, f_type, True, obj_service)
        # OTRAS MANERAS DE INVOCAR EL SELECTOR
        # correctos = feedback.find_all_next(
        #      'ion-icon', class_='circular-tick-holo')

        incorrect_ticks = feedback.select(
            'ion-icon[class="icon icon-correct md hydrated"]'
            ':not(.circular-tick-holo,.circular-tick)')  # v4
        _process_feeback_ticks(incorrect_ticks, exam_number,
                               f_question_text, f_type, False, obj_service)
        # OTRAS MANERAS DE INVOCAR EL SELECTOR
        # v0#'circular-x' #para los incorrectos
        # v1#feedback.select('ion-icon[class="icon icon-correct md hydrated"]')
        # v2#feedback.select('ion-icon:not(.circular-tick-holo,.circular-tick)')
        # v3#feedback.select('ion-icon[class="icon icon-correct md hydrated"]')
        #   .select('ion-icon:not(.circular-tick-holo,.circular-tick)')

        print(f'Q{contador_preguntas} - END')
        logger.info(f'Q{contador_preguntas} - END')
    driver.quit()  # driver.close()


if __name__ == "__main__":
    try:
        main()
        logger.info('fin')
        sys.exit(0)
    except Exception as e:
        logger.error(str(e), exc_info=True)
        sys.exit(1)
