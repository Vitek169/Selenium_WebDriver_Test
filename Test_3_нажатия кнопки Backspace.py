import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, "//input[@id ='user-name']")
user_name.send_keys(login_standard_user)
print('Input Login')
user_name.send_keys(Keys.BACKSPACE)
time.sleep(2)
user_name.send_keys(Keys.BACKSPACE)
time.sleep(2)
user_name.send_keys('er')


password = driver.find_element(By.XPATH, "//input[@id ='password']")
password.send_keys(password_all)
print('Input password')
password.send_keys(Keys.RETURN)

filter = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select')
filter.click()
print('Click Filter')
time.sleep(5)
filter.send_keys(Keys.DOWN)
time.sleep(5)
filter.send_keys(Keys.RETURN)