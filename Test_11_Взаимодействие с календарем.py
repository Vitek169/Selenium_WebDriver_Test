import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)

# radio_button = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
# radio_button.click()
action = ActionChains(driver)
duble = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
action.double_click(duble).perform()

right_click = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
action.context_click(right_click).perform()
