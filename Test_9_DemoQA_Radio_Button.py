import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



base_url = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)

radio_button = driver.find_element(By.XPATH,'//*[@id="HTMLFormElements"]/table/tbody/tr[6]/td/input[3]')
radio_button.click()
print('Click Radio Button')
time.sleep(2)

driver.close()

