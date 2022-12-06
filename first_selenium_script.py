"""First selenium script.

Returns:
    _type_: _description_
"""

import configparser
import logging
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from threading import Thread
logger = logging.getLogger('scrapping01')
logger.setLevel(logging.INFO)
logger.info('inicio')

config = configparser.ConfigParser()
config.read('config.ini')

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


ButtonContinue = safe_find_element(
    browser, By.XPATH,
    '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button',
)
ButtonContinue.click()

ButtonContinue2 = safe_find_element(
    browser, By.XPATH,
    '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button[2]')
ButtonContinue2.click()

# ANSWERING QUESTIONS WITH REAL OR UNREAL DATA
while True:
    DivQuestion = safe_find_element(
        browser, By.XPATH,
        '/html/body/div/ion-app/div/div[1]/ion-content/div/div[2]/div/div[4]/div/ion-card/ion-card-content/div/ion-list/ion-list-header/div/div')

    if DivQuestion:
        print(DivQuestion.text)

        # CHECKBOXES
        a_block_of_answers = browser.find_elements(
            By.XPATH,
            '//*[starts-with(@id, "question-")]/ion-card/ion-card-content/div/ion-list/ion-item')
        if not a_block_of_answers:
            # RADIO BUTTONS
            a_block_of_answers = browser.find_elements(
                By.XPATH,
                '//*[starts-with(@id, "question-")]/ion-card/ion-card-content/div/ion-list/ion-radio-group/ion-item')

        for answer in a_block_of_answers:
            browser.execute_script(
                "arguments[0].scrollIntoView(true);", answer)
            answer.click()

        ButtonNext = browser.find_element(
            By.CSS_SELECTOR, "ion-button[data-cy='continue-btn']")
        ButtonNext.click()
        time.sleep(1)
    else:
        break

# SCANNING CORRECT ANSWERS FROM FEEDBACK PAGE
page_source = browser.page_source
soup = BeautifulSoup(page_source, 'lxml')

feedbacks = soup.find_all('div', class_='feedback')
for feedback in feedbacks:
    print(feedback.text)
    # just to separate the feedbacks
    print('-------------------------------------')

# # byid
# cart = safe_find_element(browser, By.ID, 'site-header-cart')
# print(f'site-header-cart => {cart}')
# print(f'tipo => {type(cart)}')
# cart_text = cart.text
# print(f'cart_text => {cart_text}')

# # byid
# search_field = browser.find_element(
#     By.ID, 'woocommerce-product-search-field-0')
# search_field.send_keys('Hoddie')
# search_field.send_keys(Keys.ENTER)

# # byCSSselector
# # miMenuMyAccount = browser.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9.current_page_item > a')
# miMenuMyAccount = browser.find_element(
#     By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]')
# miMenuMyAccount.click()

# browser.quit()
# browser.close()
