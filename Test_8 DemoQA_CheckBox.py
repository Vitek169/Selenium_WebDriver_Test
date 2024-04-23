import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)

check_box = driver.find_element(By.XPATH, '//span[@class="rct-checkbox"]')
check_box.click()

"""Проверяем по тексту, что тест с ввыбором и постановкой галочки выполнен"""
text_1 = 'You have selected :'
text_in_site = driver.find_element(By.XPATH, '//*[@id="result"]/span[1]')
value_text_in_site = text_in_site.text
print(value_text_in_site)
assert text_1 == value_text_in_site
print('GOOD!')
"""Отключаем галочку"""
check_box.click()

"""Разворачиваем вкладку Home"""
home_button = driver.find_element(By.XPATH, '//button[@aria-label="Toggle"]')
home_button.click()

downloads_button = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/label/span[3]')
"""Проверяем, что вкладка Home успешно открылась на основе папки Downloads, выведя ее в качестве текста"""
value_downloads_button = downloads_button.text
print(f'{value_downloads_button}, test successful!')