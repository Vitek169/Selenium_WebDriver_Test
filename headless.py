import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")  # Для выполнения тестов без открытия браузера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
base_url = 'https://www.saucedemo.com'
driver.get(base_url)
driver.maximize_window()

login = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login)
print('Input Login')
user_password = driver.find_element(By.XPATH, '//input[@id="password"]')
user_password.send_keys(password_all)
print('Input Password')
login_button = driver.find_element(By.CSS_SELECTOR,'#login-button')
login_button.click()
print('Click Button')
# logs_product = driver.find_element(By.XPATH, '//span[@class="title"]')
# value_logs_products = logs_product.text
# print(value_logs_products)
# assert value_logs_products == "Products"
# print('Good')


"""Проверка по URL"""
url = 'https://www.saucedemo.com/inventory.html'
get_url = driver.current_url
print(get_url)
assert url == get_url
print('Good url')

driver.close()
