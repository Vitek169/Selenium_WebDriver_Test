import datetime
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)

faker = Faker('en_US')

name = faker.first_name() + str(faker.random_int())
print(name)
password = faker.password()
print(password)

user_name = driver.find_element(By.XPATH, "//input[@id ='user-name']")
user_name.send_keys(name)
print('Input Login')
password_user = driver.find_element(By.XPATH, "//input[@id ='password']")
password_user.send_keys(password)
print('Input password')
# button_login = driver.find_element(By.XPATH, "//input[@id ='login-button']")
# button_login.click()
# print('Click Logon Button')

time.sleep(2)
driver.close()


