import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)

