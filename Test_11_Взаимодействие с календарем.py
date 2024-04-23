import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)

new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
# new_date.send_keys(Keys.CONTROL + 'a') # Выделяем текст в поле
# new_date.send_keys(Keys.BACKSPACE) # Одним нажатием удаляем выделенный текст в поле
#
# time.sleep(1)
# new_date.send_keys('06/16/2024')
# time.sleep(1)
# new_date.send_keys(Keys.RETURN)

new_date.click()
time.sleep(1)
date_23 = driver.find_element(By.XPATH, '//div[contains(@class,"react-datepicker__day--today")]') # Выбор части необходимого селектора, заключения его в контейнер, для того, что бы не привязываться к конкретной дате на календаре и выборе даты сегодняшнего дня
date_23.click()
time.sleep(2)




