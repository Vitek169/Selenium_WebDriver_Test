import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
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

# driver.execute_script('window.scrollTo(0, 200')
action = ActionChains(driver)
red_t_short = driver.find_element(By.XPATH, '//*[@id="item_2_img_link"]/img"]')
action.move_to_element(red_t_short).perform()

time.sleep(3)

now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')# Возвращает дату. Задает Годд. Месяц. День. Час. Минуты. Секунд.
name_screenshot = 'screenshot' + now_date + '.png'
driver.save_screenshot('D:\\QA\\Dev_Selenium_Python\\Screen\\' + name_screenshot) #Скриншот экрана



