import datetime
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = 'https://www.lambdatest.com/selenium-playground/simple-form-demo'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)

# massage = 'Hello World'
# text_pole = driver.find_element(By.XPATH, '//input[@id="user-message"]')
# text_pole.click()
# text_pole.send_keys(massage)
# print('Input Pole')
#
# get_checked_value_button = driver.find_element(By.XPATH, '//button[@id="showInput"]')
# get_checked_value_button.click()
# print('Messege sent')
#
# text_pole_value = driver.find_element(By.XPATH, '//p[@id="message"]')
# print(text_pole_value.text)
# assert text_pole_value.text == massage
# print('Test Is Good')

num_1 = 123
num_2 = 101
num_3 = num_1 + num_2
print(num_3)
input_pole_1 = driver.find_element(By.XPATH, '//input[@id="sum1"]')
input_pole_1.click()
input_pole_1.send_keys(num_1)
print('Nam_1 Enter')

input_pole_2 = driver.find_element(By.XPATH, '//input[@id="sum2"]')
input_pole_2.click()
input_pole_2.send_keys(num_2)
print('Nam_2 Enter')

get_sum_button = driver.find_element(By.XPATH, '(//button[@type="button"])[2]')
get_sum_button.click()
print('Sum Button Click')

result_sum_value = driver.find_element(By.XPATH, '//p[@id="addmessage"]')
print(result_sum_value.text)
assert result_sum_value.text == str(num_3)
print('Sum Is Good')

time.sleep(2)
driver.close()


