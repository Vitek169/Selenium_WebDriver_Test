import datetime
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
#
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#
# base_url = 'https://www.saucedemo.com/'
# driver.get(base_url)
# driver.maximize_window()
# time.sleep(1)
#
#
# login_standard_user = 'standard_user'
# password_all = 'secret_sauce'
#
# user_name = driver.find_element(By.XPATH, "//input[@id ='user-name']")
# user_name.send_keys(login_standard_user)
# print('Input Login')
# password = driver.find_element(By.XPATH, "//input[@id ='password']")
# password.send_keys(password_all)
# print('Input password')
# button_login = driver.find_element(By.XPATH, "//input[@id ='login-button']")
# button_login.click()
# print('Click Logon Button')
# time.sleep(2)
#
# """Создаем экземпляр класса библиотеки Select Selenium для работы с селекторами"""
# select = Select(driver.find_element(By.XPATH,'//select[@data-test="product-sort-container"]'))
#
# """Обращение к селектору (дроп боксу) по видимой части"""
# #select.select_by_visible_text('Name (Z to A)')
#
# """Ищем по знаению Velue"""
# select.select_by_value('za')
driver.get('https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo')
driver.maximize_window()

drop_down = driver.find_element(By.XPATH, "//span[@class='select2-selection__arrow']")
drop_down.click()
print('Click Drop Down')
time.sleep(1)


"""Обращение к нужному элементу дроп дауна по индексу"""
# click_country = driver.find_element(By.XPATH, '(//li[@class="select2-results__option"])[4]')
# click_country.click()
# print('Click Country')

"""Выбор поля для ввода названия нужного элемента"""
input_country = driver.find_element(By.XPATH, '(//input[@class="select2-search__field"])[2]')
input_country.send_keys('Denmark')
time.sleep(1)
input_country.send_keys(Keys.RETURN)
print('Input Country')
time.sleep(1)


time.sleep(1)

driver.close()
