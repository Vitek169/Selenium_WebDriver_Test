import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)

# visible_button = driver.find_element(By.XPATH,'//button[@id="visibleAfter"]')
# visible_button.click()
# print('Click Visible Button')
time.sleep(2)

driver.close()

