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

login_standard_user = 'standard_use'
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

warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
velue_warring_text = warring_text.text
assert velue_warring_text == 'Epic sadface: Username and password do not match any user in this service'
print('Not Good')
time.sleep(2)

driver.refresh()