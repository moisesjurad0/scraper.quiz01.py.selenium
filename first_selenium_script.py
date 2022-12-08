"""First selenium script.

Returns:
    _type_: _description_
"""
import configparser
import logging
import sys
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from threading import Thread
logging.basicConfig(filename='myfirstlog.log', level=logging.DEBUG,
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
logger = logging.getLogger('scrapping01')
logger.setLevel(logging.INFO)
logger.info('inicio')

config = configparser.ConfigParser()
config.read('config.ini')


def main():
    driver_path = config['DEFAULT']['driver_path']
    brave_path = config['DEFAULT']['brave_path']
    exam_url = config['DEFAULT']['exam_url']
    quiz_url = config['DEFAULT']['quiz_url']

    service = Service(driver_path)
    options = Options()
    options.binary_location = brave_path
    # ua = UserAgent()
    # userAgent = ua.random
    # log.info(userAgent)
    # opts_chrome.add_argument(f'user-agent={userAgent}')
    # opts_chrome.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')
    # opts_chrome.add_argument("headless")
    options.add_argument("start-maximized")
    options.add_argument("--incognito")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("disable-extensions")
    options.add_argument("allow-insecure-localhost")
    options.add_argument("ignore-ssl-errors=yes")
    options.add_argument("ignore-certificate-errors")
    options.add_argument("--log-level=3")

    # Create new Instance of Chrome
    browser = webdriver.Chrome(service=service, options=options)

    browser.get(quiz_url)
    browser.implicitly_wait(5)
    print(f'titulo de la pagina => {browser.title}')
    logger.info(f'titulo de la pagina => {browser.title}')

    def safe_find_element(browser_in, the_type, selector):
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

    btn_continue = safe_find_element(
        browser, By.XPATH,
        '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button',
    )
    btn_continue.click()

    btn_continue2 = safe_find_element(
        browser, By.XPATH,
        '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button[2]')
    btn_continue2.click()

    contadorDePreguntas = 0

    # ANSWERING QUESTIONS WITH REAL OR UNREAL DATA
    while True:
        div_question = safe_find_element(
            browser, By.XPATH,
            '/html/body/div/ion-app/div/div[1]/ion-content/div/div[2]/div/div[4]/div/ion-card/ion-card-content/div/ion-list/ion-list-header/div/div')

        if div_question:
            print(div_question.text)
            contadorDePreguntas += 1

            # CHECKBOXES or RADIO BUTTONS
            a_block_of_answers = browser.find_elements(
                By.XPATH,
                '//*[starts-with(@id, "question-")]/ion-card/ion-card-content/div/ion-list/ion-item'
                ' | '
                '//*[starts-with(@id, "question-")]/ion-card/ion-card-content/div/ion-list/ion-radio-group/ion-item')

            if contadorDePreguntas == 30:
                logger.info('30')
                print('30')

            for answer in a_block_of_answers:
                browser.execute_script(
                    "arguments[0].scrollIntoView(true);", answer)
                answer.click()

            btn_next_or_finish_now = browser.find_element(
                By.CSS_SELECTOR,
                'ion-button[data-cy="continue-btn"]'
                ','
                'ion-button[data-cy="finish-btn"]')

            attribute_data_cy = btn_next_or_finish_now.get_attribute('data-cy')
            print(f'atributo_data_cy->{attribute_data_cy}')
            logger.info(f'atributo_data_cy->{attribute_data_cy}')

            if attribute_data_cy == 'continue-btn':
                btn_next_or_finish_now.click()
                time.sleep(1.5)
            elif attribute_data_cy == 'finish-btn':
                # seccion del boton "Confirm finish"
                time.sleep(2)
                btn_next_or_finish_now.click()
                time.sleep(2)
                # seccion del boton "Confirm finish now"
                btn_confirm_finish_now = browser.find_element(
                    By.XPATH,
                    '//*[@id="test_confirm_finish"]')
                btn_confirm_finish_now.click()
                time.sleep(2)
                break
        else:
            break

    # SCANNING CORRECT ANSWERS FROM FEEDBACK PAGE
    page_source = browser.page_source
    soup = BeautifulSoup(page_source, 'lxml')

    feedbacks = soup.find_all('div', class_='feedback')
    for feedback in feedbacks:
        print(feedback.text)
        #logger.info(feedback.text)
        # just to separate the feedbacks
        # print('-------------------------------------')
        # correctos = feedback.find_all_next('ion-icon', class_='circular-tick-holo')  # 'circular-x'

        # radio question
        flag_radio_question = False
        try:
            f_question_text = (feedback.contents[0].contents[0].next_sibling.
                               contents[0].contents[0].contents[0].contents[0].contents[0].next_element)
            flag_radio_question = True
        except Exception as e:
            logger.error(str(e), exc_info=True)

        # check question or maybe radio question too
        flag_check_question = False
        if not flag_radio_question:
            try:
                f_question_text = (feedback.contents[0].contents[0].next_sibling.
                                   div.contents[0].contents[0].contents[0].contents[0].contents[0].next_element)
                flag_check_question = True
            except Exception as e:
                logger.error(str(e), exc_info=True)

        print(f_question_text)
        logger.info(f_question_text)

        if flag_radio_question:
            correct_radios = feedback.find_all('ion-icon', class_='circular-tick-holo')
            for correct_option in correct_radios:
                # bs4.element.NavigableString
                f_correct_answer_text = correct_option.previous_sibling.div.div.next_sibling.div.next_element
                print(f_correct_answer_text)
                logger.info(f_correct_answer_text)
        elif flag_check_question:
            correct_checks = feedback.find_all('ion-icon', class_='circular-tick')
            for correct_option in correct_checks:
                # aun no he probado que funcione con checkboxes
                f_correct_answer_text = correct_option.previous_sibling.div.div.next_sibling.div.next_element
                print(f_correct_answer_text)
                logger.info(f_correct_answer_text)



    # browser.quit()
    # browser.close()


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except Exception as e:
        logger.error(str(e), exc_info=True)
        sys.exit(1)
