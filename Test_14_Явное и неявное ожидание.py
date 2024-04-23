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

login_standard_user = 'standard_user'
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
time.sleep(5)

menu = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
menu.click()
print('Click Menu Button')
time.sleep(2)

link_about = driver.find_element(By.XPATH, '//a[@id="about_sidebar_link"]')
link_about.click()
print('Click Link Button')
time.sleep(2)

driver.back()
print('Go Back')
time.sleep(2)
driver.forward()
print('Go Forward')