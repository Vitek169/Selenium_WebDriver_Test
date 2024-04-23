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
# text_products = driver.find_element(By.XPATH, "//span[@class='title']")
# value_text_ptoducts = text_products.text
# print(value_text_ptoducts)
# assert value_text_ptoducts == 'PRODUCTS'
# print('Good')
now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')# Возвращает дату. Задает Годд. Месяц. День. Час. Минуты. Секунд.
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('D:\\QA\\Dev_Selenium_Python\\Screen\\' + name_screenshot) #Скриншот экрана

url = 'https://www.saucedemo.com/inventory.html'
get_url = driver.current_url
print(get_url)
assert url == get_url
print('Good URL')
