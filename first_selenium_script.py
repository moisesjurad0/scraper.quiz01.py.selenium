from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com/')
driver.implicitly_wait(3)
print(f'titulo de la pagina => {driver.title}')

# byid
cart = driver.find_element(By.ID, 'site-header-cart')
print(f'site-header-cart => {cart}')
print(f'tipo => {type(cart)}')
cart_text = cart.text
print(f'cart_text => {cart_text}')

# byid
search_field = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
search_field.send_keys('Hoddie')
search_field.send_keys(Keys.ENTER)

# byCSSselector
#miMenuMyAccount = driver.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9.current_page_item > a')
miMenuMyAccount = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]')
miMenuMyAccount.click()

# driver.quit()
# driver.close()
