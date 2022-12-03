import configparser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
browser.implicitly_wait(2)
print(f'titulo de la pagina => {browser.title}')

# ButtonStartAssesment = browser.find_element(
#     By.XPATH,
#     '//*[@id="block-scrumorg-v2-content"]/article/div/section[3]/div/div/div/div/div/p[6]/a')
# ButtonStartAssesment.click()
ButtonContinue = browser.find_element(
    By.XPATH,
    '//*[@id="app"]/ion-app/div/div[1]/ion-content/div/div[3]/ion-button')
ButtonContinue.click()
















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
