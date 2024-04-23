import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, "//input[@id ='user-name']")
user_name.send_keys(login_standard_user)
print('Input Login')
password = driver.find_element(By.XPATH, "//input[@id ='password']")
password.send_keys(password_all)
print('Input password')
button_login = driver.find_element(By.XPATH, "//input[@id ='login-button']")
button_login.click()
print('Click Logon Button')
time.sleep(1)

"""Info Product 1"""
product_1 = driver.find_element(By.XPATH, "//a[@id = 'item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print('Select Product 1')
time.sleep(1)

cart = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
cart.click()
print('Enter Cart')
time.sleep(1)

"""Info Cart Product 1"""
cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print('Info Cart Product 1 Good')

price_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_cart_product_1 = price_cart_product_1.text
print(value_price_cart_product_1)
assert value_price_product_1 == value_price_cart_product_1
print('Info Cart Price Product 1 Good')

checkout_button = driver.find_element(By.XPATH, "//button[@id = 'checkout']")
checkout_button.click()
print('Klick Checkout')
time.sleep(1)

"""Enter Data Person"""
first_name = 'Viktor'
last_name = '169'
code = 'TRON'

enter_fist_name = driver.find_element(By.XPATH, "//input[@id = 'first-name']")
enter_fist_name.send_keys(first_name)
print('Input First Name')
time.sleep(1)

enter_last_name = driver.find_element(By.XPATH, "//input[@id = 'last-name']")
enter_last_name.send_keys(last_name)
print('Input Last Name')
time.sleep(1)

enter_cod = driver.find_element(By.XPATH, "//input[@id = 'postal-code']")
enter_cod.send_keys(code)
print('Input Zip Cod')
time.sleep(1)

continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print('Click Button Continue')
time.sleep(1)

"""Info Finish Product 1"""
finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print('Info Finish Product 1 Good')

price_finish_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_finish_product_1 = price_finish_product_1.text
print(value_price_finish_product_1)
assert value_price_product_1 == value_price_finish_product_1
print('Info Finish Price Product 1 Good')

summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[5]")
value_summary_price = summary_price.text
print(value_summary_price)
item_total = f'Item total: {value_price_finish_product_1}'
print(item_total)
assert value_summary_price == item_total
print('Total Suumary Price Good!')

"""Finish"""
finish_button = driver.find_element(By.XPATH, "//button[@id = 'finish']")
finish_button.click()
print('Finish page')

thank_order = driver.find_element(By.XPATH, "//*[@id='checkout_complete_container']/h2")
value_thank_order = thank_order.text
print(f'{value_thank_order} Test Finish Good!')
print('Test finish - GOOD!')