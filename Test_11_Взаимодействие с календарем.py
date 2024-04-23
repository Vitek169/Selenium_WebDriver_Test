import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)

new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
new_date.send_keys(Keys.CONTROL + 'a') # Выделяем текст в поле
new_date.send_keys(Keys.BACKSPACE) # Одним нажатием удаляем выделенный текст в поле

time.sleep(1)
new_date.send_keys('06/16/2024')
time.sleep(1)
new_date.send_keys(Keys.RETURN)




