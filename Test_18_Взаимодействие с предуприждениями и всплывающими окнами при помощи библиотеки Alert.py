import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(base_url)
driver.maximize_window()

click_button_alert_1 = driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]')
click_button_alert_1.click()
print('Click Button One')
time.sleep(2)

driver.switch_to.alert.accept() # Выбрали метод Accept для подтверждения

text_value = driver.find_element(By.XPATH,'//p[@id="result"]')
print(text_value.text)
time.sleep(2)

click_button_alert_2 = driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]')
click_button_alert_2.click()
print('Click Button Two')
time.sleep(2)

driver.switch_to.alert.dismiss() # Выбрали метод Dismiss для отклонения

text_value = driver.find_element(By.XPATH,'//p[@id="result"]')
print(text_value.text)
time.sleep(2)


driver.close()




