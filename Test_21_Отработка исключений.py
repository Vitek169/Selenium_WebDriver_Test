import datetime
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



# base_url = 'https://demoqa.com/dynamic-properties' # Для Try Except
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)
"""Пишем отлов исключения"""
# try:
#     visible_button = driver.find_element(By.XPATH,'//button[@id="visibleAfter"]')
#     visible_button.click()
# except NoSuchElementException as exception:
#     print('NoSuchElementException')
#     time.sleep(10)
#     visible_button = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
#     visible_button.click()
#     print('Click Visible Button')


yes_checkbox = driver.find_element(By.XPATH,'//label[@for="yesRadio"]')
yes_checkbox.click()
try:
    message = driver.find_element(By.XPATH,'//span[@class="text-success"]')
    value_massage = message.text
    print(value_massage)
    assert value_massage == "No"
except AssertionError as exception:
    driver.refresh()
    yes_checkbox = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
    yes_checkbox.click()
    message = driver.find_element(By.XPATH, '//span[@class="text-success"]')
    value_massage = message.text
    assert value_massage == "Yes"
    print('Checkbox YES')
print('Test over')

driver.close()

