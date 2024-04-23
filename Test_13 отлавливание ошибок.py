import datetime
import time

from selenium import webdriver
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

new_date = driver.find_element(By.XPATH, '//input[@id = "datePickerMonthYearInput"]')
new_date.click()
# for i in range(10):
#     new_date.send_keys(Keys.BACKSPACE)
time.sleep(2)
# new_date.send_keys('02/14/2023')
# new_date.send_keys(Keys.RETURN)

next_day = driver.find_element(By.XPATH, '//div[@aria-label="Choose Friday, February 17th, 2023"]')
next_day.click()
