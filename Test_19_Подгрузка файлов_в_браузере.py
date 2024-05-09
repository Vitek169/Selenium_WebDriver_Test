import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'
driver.get(base_url)
driver.maximize_window()
time.sleep(2)

path_file = '/home/vitek169/it/Selenium_WebDriver_Test/fils/Viking.jpg'

click_button = driver.find_element(By.XPATH, '//input[@id="file"]')
click_button.send_keys(path_file)
text_result = driver.find_element(By.XPATH, '//div[@id="error"]')
print(text_result.text)


time.sleep(2)
driver.close()




