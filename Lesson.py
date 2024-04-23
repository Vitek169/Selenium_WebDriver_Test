import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://www.saucedemo.com/')
driver.maximize_window()
user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys('standard_user')
password = driver.find_element(By.ID, 'password')
password.send_keys('secret_sauce')
button_login =driver.find_element(By.ID, 'login-button')
button_login.click()