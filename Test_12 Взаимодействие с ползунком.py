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

base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()

action = ActionChains(driver)

filter_def = driver.find_element(By.XPATH, '//input[@type="range"]')


"""метод кликнуть и тянуть ползунок click_and_hold() и метод перемещение по горизонтали и вертикали move_by_offset(), после чего метод отпускания мыши release() и метод сохранения резульата perform()"""
action.click_and_hold(filter_def).move_by_offset(-30, 0).release().perform()
print('Бегунок сдвинулся')

time.sleep(1)
driver.close()





