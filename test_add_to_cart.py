from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()

def scroll_to(element):
    location = element.location_once_scrolled_into_view
    driver.execute_script("window.scrollTo({}, {});".format(0, location['y']))

def test_add_to_cart():
    driver.get('https://goodhoodstore.com')

    wait = WebDriverWait(driver, 10)
    country_selector = '.sec-StoreSelector_Content[aria-hidden="false"] button.sec-StoreSelector_Button'
    item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, country_selector)))
    country_selector_button = driver.find_element(By.CSS_SELECTOR, country_selector)
    country_selector_button.click()

    search_bar = driver.find_element(By.ID, 'header-search')
    search_bar.send_keys('press', Keys.ENTER)

    item_selector = '.prd-Card'
    wait = WebDriverWait(driver, 10)
    item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, item_selector)))
    item = driver.find_element(By.CSS_SELECTOR, item_selector)
    scroll_to(item)
    item.click()


    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, '.prd-Details_Button[name="add"]')
    scroll_to(add_to_cart_button)
    add_to_cart_button.click()
    sleep(1)

    product_name = driver.find_element(By.CSS_SELECTOR, '.prd-Details_Title').text

    driver.get('https://goodhoodstore.com/cart')

    cart_element = driver.find_element(By.CSS_SELECTOR, '.crt-Cart_Products')
    cart_html = cart_element.get_attribute('outerHTML')
    assert product_name in cart_html

    driver.quit()
