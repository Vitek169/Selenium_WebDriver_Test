import datetime
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



# base_url = 'https://demoqa.com/dynamic-properties' # Для Try Except
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
# driver.maximize_window()
time.sleep(1)

# print('Start Test')
# driver.implicitly_wait(10) # Ожидание
# visible_button = driver.find_element(By.XPATH,'//button[@id="visibleAfter"]')
# visible_button.click()
# print('Finish Test')



print('Start Test')
visible_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="visibleAfter"]')))
visible_button.click()
print('Finish Test')
