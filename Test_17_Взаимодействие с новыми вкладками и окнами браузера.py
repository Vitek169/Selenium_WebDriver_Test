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

driver.get('https://demoqa.com/browser-windows')
driver.maximize_window()


"""Переключение между вкладками"""
# new_tab_button = driver.find_element(By.XPATH, "//button[@id='tabButton']")
# new_tab_button.click()
# print("Click Tab URL", driver.current_url, sep='\n')
# heder_1 = driver.find_element(By.XPATH, '//h1[@class="text-center"]')
# print(heder_1.text)
#
# driver.switch_to.window(driver.window_handles[1])
# print(driver.current_url)
#
# heder_2 = driver.find_element(By.XPATH, '//h1[@id="sampleHeading"]')
# print(heder_2.text)
#
# driver.switch_to.window(driver.window_handles[1])
# print(driver.current_url)

"""Взаимодействие с новым окном переключение"""

new_windows_button = driver.find_element(By.XPATH, '//button[@id="windowButton"]')
new_windows_button.click()
heder_1 = driver.find_element(By.XPATH, '//h1[@class="text-center"]')
print("Click New Window", driver.current_url, heder_1.text, sep='\n')

windows_1 = driver.window_handles[0]
windows_2 = driver.window_handles[1]

driver.switch_to.window(windows_2)
print(driver.current_url)

heder_2 = driver.find_element(By.XPATH, '//h1[@id="sampleHeading"]')
print(heder_2.text)


driver.switch_to.window(windows_1)
print(driver.current_url, heder_1.text, sep='\n')

time.sleep(5)
driver.close()