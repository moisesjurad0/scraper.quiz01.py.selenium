"""First selenium script.

Returns:
    _type_: _description_
"""
import argparse
import configparser
import datetime
import logging
import sys
import uuid

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import my_service

currentDT = datetime.datetime.now()
logging.basicConfig(
    filename=f'scrap01{currentDT.strftime("%Y%m%d%H%M%S")}.log',
    level=logging.INFO,
    format='%(asctime)s | %(name)s | %(levelname)s | [%(filename)s:%(lineno)d] | %(message)s')
logger = logging.getLogger('scrapping01')
logger.setLevel(logging.INFO)
logger.info('inicio')

config = configparser.ConfigParser()
config.read('config.ini')
ew = 20  # ew stands for explicit_wait


def _analyze_question(feedback) -> {str, str}:
    """Determinar el tipo de pregunta."""
    input_type = ''
    question_text = ''

    try:
        question_text = (
            feedback.contents[0].contents[0].next_sibling.
            contents[0].contents[0].contents[0].contents[0].contents[0].next_element)
        input_type = 'RADIO'
    except Exception as e1:
        logger.warning(str(e1), exc_info=True)

        try:
            question_text = (
                feedback.contents[0].contents[0].next_sibling.div.
                contents[0].contents[0].contents[0].contents[0].contents[0].next_element)
            input_type = 'CHECK'

            if question_text == 'True or False:':
                input_type = 'RADIO_BOOL'
                question_text = question_text.next_element

            elif question_text[-1] == ' ':
                if str(question_text.next_element.next_element) == 'NOT':
                    question_text = (
                        f'{question_text}'
                        f'{question_text.next_element.next_element}'
                        f'{question_text.next_element.next_element.next_element}')

        except Exception as e2:
            logger.error(str(e2), exc_info=True)

    return input_type, question_text


def _mark_dom_answers(driver, scrapped_answers_to_choose):
    for scrapped_answer in scrapped_answers_to_choose:
        _roll_n_click_to_answer(driver, scrapped_answer)


def _roll_n_click_to_answer(driver, scrapped_answer):
    driver.execute_script("arguments[0].scrollIntoView(true);", scrapped_answer)
    # browser.execute_script("arguments[0].click();", answer)
    # answer.click()
    WebDriverWait(driver, ew).until(EC.element_to_be_clickable(scrapped_answer)).click()


def main():
    parser = argparse.ArgumentParser(description='Scraper0X')
    parser.add_argument(
        '-n',
        '--examnumber',
        required=False,
        help='Parametro para decidir que examen ejecutar. Dejarlo vacio usa el default del config.ini',
        default='0')
    args = parser.parse_args()
    logger.info('*************** PARAMETROS DE ENTRADA => '
                f'--examnumber:{args.examnumber}'
                ' ***************')

    if args.examnumber == '0':
        exam_number = config['DEFAULT']['exam_to_do']
    else:
        exam_number = args.examnumber

    exam_section = f'EXAM-{exam_number}'
    quiz_url = config[exam_section]['quiz_url']
    x_api_key = config[exam_section]['x-api-key']
    api_put = config[exam_section]['api_put']
    api_search = config[exam_section]['api_search']

    obj_service = my_service.MyService(x_api_key, api_put, api_search)

    v_uuid = uuid.uuid4().hex
    print(f'v_uuid->{v_uuid}')
    logger.info(f'v_uuid->{v_uuid}')

    driver_path = config['DEFAULT']['driver_path']
    brave_path = config['DEFAULT']['brave_path']
    headless = config.getboolean('DEFAULT', 'headless')
    do_correct_answers = config.getboolean('DEFAULT', 'do_correct_answers')

    service = Service(driver_path)
    options = Options()
    options.binary_location = brave_path
    # ua = UserAgent()
    # userAgent = ua.random
    # log.info(userAgent)
    # opts_chrome.add_argument(f'user-agent={userAgent}')
    # opts_chrome.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    #                          '(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')
    options.add_argument("headless") if headless else None
    options.add_argument("--start-fullscreen")  # or with --
    # options.add_argument("start-maximized")
    options.add_argument("--incognito")  # or without --
    # options.add_argument("--disable-infobars") #not working on latest versions of driver
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
    # soup = BeautifulSoup(page_source, 'lxml')  # codigo para probar si tenemos lxml antes de empezar

    # default is zero - don't activate this cause will  interfere with WebDriverWait
    # driver.implicitly_wait(implicitly_wait)

    # press 1st button Next
    WebDriverWait(driver, ew).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button'))).click()

    # press 2nd button Next
    WebDriverWait(driver, ew).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button[2]'))).click()

    logger.info('SECTION - ANSWERING QUESTIONS')
    while True:
        div_xpath = (
            '/html/body/div/ion-app/div/div[1]/ion-content/div/div[2]/div/div[4]/div/'
            'ion-card/ion-card-content/div/ion-list/ion-list-header/div/div')
        try:
            WebDriverWait(driver, 3).until_not(EC.visibility_of_element_located((By.XPATH, div_xpath)))
        except Exception as ex1:
            logger.error(str(ex1), exc_info=True)
        finally:
            div_question_text = WebDriverWait(driver, ew).until(
                EC.visibility_of_element_located((By.XPATH, div_xpath))).text.split("\n")[0]
            if div_question_text.startswith('True or False: '):
                div_question_text = div_question_text.split('True or False: ')[1]
            print(div_question_text)

        # WebDriverWait(driver, ew).until(EC.invisibility_of_element_located((By.XPATH, div_xpath)))
        # div_question = WebDriverWait(driver, ew).until(EC.presence_of_element_located((By.XPATH, div_xpath)))
        # print(div_question.text)

        # CHECKBOXES or RADIO BUTTONS
        scrapped_answers_to_choose = driver.find_elements(
            By.XPATH,
            '//*[starts-with(@id, "question-")]/ion-card/ion-card-content/div/ion-list/ion-item'
            ' | '
            '//*[starts-with(@id, "question-")]/ion-card/ion-card-content/div/ion-list/ion-radio-group/ion-item')

        if do_correct_answers:
            logger.info('SECTION - DO CORRECT ANSWERS')
            stored_data = obj_service.search_v2(question=div_question_text, flag_correct=True)
            if stored_data:
                logger.info('ITEM - DATA FOUND')
                for stored_item in stored_data:
                    for scrapped_answer in scrapped_answers_to_choose:
                        scrapped_answer_txt = scrapped_answer.find_element(By.CLASS_NAME, 'bbcode, cursor-pointer').text
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
        WebDriverWait(driver, ew).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, btn_css_selector)))
        btn_next_or_finish_now = driver.find_element(By.CSS_SELECTOR, btn_css_selector)

        attribute_data_cy = btn_next_or_finish_now.get_attribute('data-cy')

        if attribute_data_cy == 'continue-btn':
            btn_next_or_finish_now.click()
            # WebDriverWait(driver, ew).until(EC.element_to_be_clickable(btn_next_or_finish_now)).click()
            # time.sleep(2)  # Este se encarga de waitear a la pregunta, de arriba que es donde se cae
        elif attribute_data_cy == 'finish-btn':
            # seccion del boton "Confirm finish"
            # time.sleep(2)
            btn_next_or_finish_now.click()
            # WebDriverWait(driver, ew).until(EC.element_to_be_clickable(btn_next_or_finish_now)).click()
            # time.sleep(2)
            # seccion del boton "Confirm finish now"
            # btn_confirm_finish_now = driver.find_element(By.XPATH, '//*[@id="test_confirm_finish"]')
            # btn_confirm_finish_now.click()
            WebDriverWait(driver, ew).until(
                EC.element_to_be_clickable((
                    By.XPATH, '//*[@id="test_confirm_finish"]')
                )).click()
            break

    logger.info('HACER UN WAIT DE LA PAGINA DE RESULTADO, DEL LA PARTE DE ARRIBA Y LA DE ABAJO DE LA PAGINA')

    # WebDriverWait(driver, ew).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logo-area"]/div/div/img')))
    WebDriverWait(driver, ew).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/ion-card[1]')))
    WebDriverWait(driver, ew).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/ion-card[2]')))
    WebDriverWait(driver, ew).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/div')))

    logger.info('SCANNING CORRECT ANSWERS FROM FEEDBACK PAGE')

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    contador_preguntas = 0
    feedbacks = soup.find_all('div', class_='feedback')
    for feedback in feedbacks:
        contador_preguntas += 1
        print(feedback.text)
        # logger.info(feedback.text)
        # just to separate the feedbacks
        # print('-------------------------------------')
        # correctos = feedback.find_all_next('ion-icon', class_='circular-tick-holo')  # 'circular-x'

        f_type, f_question_text = _analyze_question(feedback)

        print(f'Q{contador_preguntas} - {f_question_text}')
        logger.info(f'Q{contador_preguntas} - {f_question_text}')

        correct_ticks = feedback.select('.circular-tick, .circular-tick-holo')
        for correct_option in correct_ticks:
            if f_type == 'RADIO_BOOL':
                f_correct_answer_text = (correct_option.previous_sibling.
                                         next_element.next_element.next_element.next_element.next_element)
            else:
                f_correct_answer_text = (correct_option.previous_sibling.
                                         next_element.next_element.next_element.next_element.next_element.next_element)
            print(f_correct_answer_text)
            logger.info(f_correct_answer_text)
            obj_service.put(f'{f_question_text}---{f_correct_answer_text}',
                            f_question_text, f_type, f_correct_answer_text, True, exam_number, currentDT.isoformat())

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
