"""First selenium script.

Returns:
    _type_: _description_
"""
import configparser
import datetime
import logging
import sys
import time
import uuid

import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import send

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


def _safe_find_element(browser_in, the_type, selector):
    """Buscar elemento de manera segura.

    Args:
        browser_in (_type_): _description_
        the_type (_type_): _description_
        selector (_type_): _description_

    Returns:
        _type_: _description_
    """
    obj_element = None
    try:
        obj_element = browser_in.find_element(
            the_type,
            selector)
    except Exception as e:
        logger.warning(e, exc_info=True)
    return obj_element


def _determine_question_type(feedback) -> {str, bs4.element.NavigableString}:
    """Determinar el tipo de pregunta."""
    input_type = ''
    question_text = bs4.NavigableString('')

    try:
        question_text = (
            feedback.contents[0].contents[0].next_sibling.
            contents[0].contents[0].contents[0].contents[0].contents[0].next_element)
        input_type = 'RADIO'
    except Exception as e1:
        logger.error(str(e1), exc_info=True)
        try:
            question_text = (
                feedback.contents[0].contents[0].next_sibling.div.
                contents[0].contents[0].contents[0].contents[0].contents[0].next_element)
            if question_text == 'True or False:':
                input_type = 'RADIO'
                question_text = question_text.next_element
            else:
                input_type = 'CHECK'
        except Exception as e2:
            logger.error(str(e2), exc_info=True)

    return input_type, question_text


def main():
    v_uuid = uuid.uuid4().hex
    print(f'v_uuid->{v_uuid}')
    logger.info(f'v_uuid->{v_uuid}')

    driver_path = config['DEFAULT']['driver_path']
    brave_path = config['DEFAULT']['brave_path']
    quiz_url = config['DEFAULT']['quiz_url']
    implicitly_wait = config.getint('DEFAULT', 'implicitly_wait')

    service = Service(driver_path)
    options = Options()
    options.binary_location = brave_path
    # ua = UserAgent()
    # userAgent = ua.random
    # log.info(userAgent)
    # opts_chrome.add_argument(f'user-agent={userAgent}')
    # opts_chrome.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')
    # opts_chrome.add_argument("headless")
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

    if not implicitly_wait > 0:
        implicitly_wait = 5
    driver.implicitly_wait(implicitly_wait)

    btn_continue = _safe_find_element(
        driver, By.XPATH,
        '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button',
    )
    btn_continue.click()

    btn_continue2 = _safe_find_element(
        driver, By.XPATH,
        '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button[2]')
    btn_continue2.click()

    print('ANSWERING QUESTIONS WITH UNREAL DATA')
    logger.info('ANSWERING QUESTIONS WITH REAL OR UNREAL DATA')
    while True:
        div_question = _safe_find_element(
            driver, By.XPATH,
            '/html/body/div/ion-app/div/div[1]/ion-content/div/div[2]/div/div[4]/div/ion-card/ion-card-content/div/ion-list/ion-list-header/div/div')

        if div_question:
            print(div_question.text)

            # CHECKBOXES or RADIO BUTTONS
            a_block_of_answers = driver.find_elements(
                By.XPATH,
                '//*[starts-with(@id, "question-")]/ion-card/ion-card-content/div/ion-list/ion-item'
                ' | '
                '//*[starts-with(@id, "question-")]/ion-card/ion-card-content/div/ion-list/ion-radio-group/ion-item')

            for answer in a_block_of_answers:
                driver.execute_script("arguments[0].scrollIntoView(true);", answer)
                # browser.execute_script("arguments[0].click();", answer)
                # answer.click()
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable(answer)).click()

            btn_css_selector = (
                'ion-button[data-cy="continue-btn"]'
                ','
                'ion-button[data-cy="finish-btn"]')
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, btn_css_selector)))
            btn_next_or_finish_now = driver.find_element(
                By.CSS_SELECTOR,
                btn_css_selector)

            attribute_data_cy = btn_next_or_finish_now.get_attribute('data-cy')

            if attribute_data_cy == 'continue-btn':
                btn_next_or_finish_now.click()
                # WebDriverWait(driver, 20).until(EC.element_to_be_clickable(btn_next_or_finish_now)).click()
                time.sleep(2)  # Este se encarga de waitear a la pregunta, de arriba que es donde se cae
            elif attribute_data_cy == 'finish-btn':
                # seccion del boton "Confirm finish"
                # time.sleep(2)
                btn_next_or_finish_now.click()
                # WebDriverWait(driver, 20).until(EC.element_to_be_clickable(btn_next_or_finish_now)).click()
                # time.sleep(2)
                # seccion del boton "Confirm finish now"
                # btn_confirm_finish_now = driver.find_element(
                #     By.XPATH,
                #     '//*[@id="test_confirm_finish"]')
                # btn_confirm_finish_now.click()
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((
                        By.XPATH, '//*[@id="test_confirm_finish"]')
                    )).click()
                break
        else:
            break

    print('HACER UN WAIT DE LA PAGINA DE RESULTADO, DEL LA PARTE DE ARRIBA Y LA DE ABAJO DE LA PAGINA')
    logger.info('HACER UN WAIT DE LA PAGINA DE RESULTADO, DEL LA PARTE DE ARRIBA Y LA DE ABAJO DE LA PAGINA')
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logo-area"]/div/div/img')))
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="contents"]/ion-card[1]')))
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="contents"]/ion-card[2]')))
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="contents"]/div')))

    print('SCANNING CORRECT ANSWERS FROM FEEDBACK PAGE')
    logger.info('SCANNING CORRECT ANSWERS FROM FEEDBACK PAGE')
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')

    contador_preguntas = 0
    feedbacks = soup.find_all('div', class_='feedback')
    for feedback in feedbacks:
        contador_preguntas += 1
        print(feedback.text)
        # logger.info(feedback.text)
        # just to separate the feedbacks
        # print('-------------------------------------')
        # correctos = feedback.find_all_next('ion-icon', class_='circular-tick-holo')  # 'circular-x'

        f_type, f_question_text = _determine_question_type(feedback)

        print(f'Q{contador_preguntas} - {f_question_text}')
        logger.info(f'Q{contador_preguntas} - {f_question_text}')

        if f_type == 'RADIO':
            correct_radios = feedback.find_all('ion-icon', class_='circular-tick-holo')
            for correct_option in correct_radios:
                f_correct_answer_text = correct_option.previous_sibling.div.div.next_sibling.div.next_element
                print(f_correct_answer_text)
                logger.info(f_correct_answer_text)
                send.create(f'{f_question_text}---{f_correct_answer_text}', f_question_text, f_type,
                            f_correct_answer_text, True)
        elif f_type == 'CHECK':
            correct_checks = feedback.find_all('ion-icon', class_='circular-tick')
            for correct_option in correct_checks:
                f_correct_answer_text = correct_option.previous_sibling.div.div.next_sibling.div.next_element
                print(f_correct_answer_text)
                logger.info(f_correct_answer_text)
                send.create(f'{f_question_text}---{f_correct_answer_text}', f_question_text, f_type,
                            f_correct_answer_text, True)
        print(f'Q{contador_preguntas} - END')
        logger.info(f'Q{contador_preguntas} - END')
    driver.quit()  # browser.close()


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except Exception as e:
        logger.error(str(e), exc_info=True)
        sys.exit(1)
