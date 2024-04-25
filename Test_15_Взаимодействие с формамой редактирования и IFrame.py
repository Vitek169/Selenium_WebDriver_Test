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

base_url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)


"""Выбираем локатор iframe, заведя для нее переменную, а дальше driver.switch_to.frame() указываем, что мы обращаемся к нашей переменной iframe и после этого обращаемся к локатору поля для заполнения"""
iframe = driver.find_element(By.XPATH, '//iframe[@id="iFrame1"]')
driver.switch_to.frame(iframe)
pole = driver.find_element(By.XPATH, '//div[@id="__next"]/div/div[2]')
value_pole = pole.text
print(value_pole)
pole.send_keys(Keys.CONTROL + 'a')
editing_panel = driver.find_element(By.XPATH, '//button[@title="Bold"]')
editing_panel.click()
print('Editing Panel Click')

new_pole = driver.find_element(By.XPATH, '//div[@id="__next"]/div/div[2]/b').text
assert value_pole == new_pole
print('Редактирование успешно')











time.sleep(2)
driver.close()


