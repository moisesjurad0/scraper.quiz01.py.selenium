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

ButtonContinue = browser.find_element(
    By.XPATH,
    '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button')
ButtonContinue.click()

ButtonContinue2 = browser.find_element(
    By.XPATH,
    '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button[2]')
ButtonContinue2.click()

# ANSWERING QUESTIONS WITH REAL OR UNREAL DATA

while True:
    try:
        DivQuestion = browser.find_element(
            By.XPATH,
            # '//*[@id="question-*"]/ion-card/ion-card-content/div/ion-list/ion-list-header/div/div')
            '/html/body/div/ion-app/div/div[1]/ion-content/div/div[2]/div/div[4]/div/ion-card/ion-card-content/div/ion-list/ion-list-header/div/div')

        if DivQuestion:
            print(DivQuestion.text)

            for i in range(1, 6):

                errorOnFirst = False
                try:
                    DivCheckBoxTmp = browser.find_element(
                        By.XPATH,
                        f'/html/body/div/ion-app/div/div[1]/ion-content/div/div[2]/div/div[4]/div/ion-card/ion-card-content/div/ion-list/ion-item[{i}]')
                    # Thread.sleep(100)
                    DivCheckBoxTmp.click()
                    # Thread.sleep(100)
                except Exception as e:
                    logger.warning(e, exc_info=True)
                    errorOnFirst = True

                if errorOnFirst:
                    try:
                        DivRadioTmp = browser.find_element(
                            By.XPATH,
                            f'/html/body/div/ion-app/div/div[1]/ion-content/div/div[2]/div/div[4]/div/ion-card/ion-card-content/div/ion-list/ion-radio-group/ion-item[{i}]')
                        # Thread.sleep(100)
                        DivRadioTmp.click()
                        # Thread.sleep(100)
                    except Exception as e:
                        logger.warning(e, exc_info=True)




        else:
            break
        ButtonNext = browser.find_element(
            By.XPATH,
            '//*[@id="test-contents"]/div[5]/ion-grid/ion-row/ion-col/ion-button')
        ButtonNext.click()
        # Thread.sleep(250)
    except Exception as e:
        logger.warning(e, exc_info=True)
        break

# SCANNING CORRECT ANSWERS FROM FEEDBACK PAGE
page_source = browser.page_source
soup = BeautifulSoup(page_source, 'lxml')

feedbacks = soup.find_all('div', class_='feedback')
for feedback in feedbacks:
    print(feedback.text)
    print('-------------------------------------')  # just to separate the feedbacks

# byid
cart = browser.find_element(By.ID, 'site-header-cart')
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
