import configparser
import logging

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# from threading import Thread

logger = logging.getLogger('scrapping01')
logger.setLevel(logging.INFO)

config = configparser.ConfigParser()
config.read('config.ini')

driver_path = config['DEFAULT']['driver_path']
brave_path = config['DEFAULT']['brave_path']
exam_url = config['DEFAULT']['exam_url']
quiz_url = config['DEFAULT']['quiz_url']

service = Service(driver_path)
options = Options()
options.binary_location = brave_path
options.add_argument("start-maximized")
options.add_argument("--incognito")

# Create new Instance of Chrome
browser = webdriver.Chrome(service=service, options=options)

browser.get(quiz_url)
browser.implicitly_wait(5)
print(f'titulo de la pagina => {browser.title}')


def safeFindElement(browser_in, the_type, selector):
    retorno = None
    try:
        retorno = browser_in.find_element(
            the_type,
            selector)
    except Exception as e:
        logger.warning(e, exc_info=True)
    return retorno


ButtonContinue = safeFindElement(
    browser, By.XPATH,
    '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button',
)
ButtonContinue.click()

ButtonContinue2 = safeFindElement(
    browser, By.XPATH,
    '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button[2]')
ButtonContinue2.click()

# ANSWERING QUESTIONS WITH REAL OR UNREAL DATA
while True:
    DivQuestion = safeFindElement(
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
            browser.execute_script("arguments[0].scrollIntoView(true);", answer)
            answer.click()

        ButtonNext = safeFindElement(
            browser, By.XPATH, '//*[@id="test-contents"]/div[5]/ion-grid/ion-row/ion-col/ion-button'
        )
        ButtonNext.click()
    else:
        break

# SCANNING CORRECT ANSWERS FROM FEEDBACK PAGE
page_source = browser.page_source
soup = BeautifulSoup(page_source, 'lxml')

feedbacks = soup.find_all('div', class_='feedback')
for feedback in feedbacks:
    print(feedback.text)
    print('-------------------------------------')  # just to separate the feedbacks

# byid
cart = safeFindElement(browser, By.ID, 'site-header-cart')
print(f'site-header-cart => {cart}')
print(f'tipo => {type(cart)}')
cart_text = cart.text
print(f'cart_text => {cart_text}')

# byid
search_field = browser.find_element(By.ID, 'woocommerce-product-search-field-0')
search_field.send_keys('Hoddie')
search_field.send_keys(Keys.ENTER)

# byCSSselector
# miMenuMyAccount = browser.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9.current_page_item > a')
miMenuMyAccount = browser.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]')
miMenuMyAccount.click()

# browser.quit()
# browser.close()
