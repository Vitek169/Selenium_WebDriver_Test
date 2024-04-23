import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)

action = ActionChains(driver)
double_click = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
action.double_click(double_click).perform() # Метод ЭкшенЧейнс для двойного нажатия

right_click = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
action.context_click(right_click).perform() # Метод ЭкшенЧейнс для нажатия правой кнопки мыши


time.sleep(2)