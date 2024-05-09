import datetime
import glob
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

path_downloads = '\\home\\vitek169\\it\\Selenium_WebDriver_Test\\fils_download\\'

# options = Options()
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# prefs = {'download.default_directory' : path_downloads}
# options.add_experimental_option('prefs', prefs)
# options.add_experimental_option("detach", True)
# #
# base_url = 'https://www.lambdatest.com/selenium-playground/download-file-demo'
# driver.get(base_url)
# driver.maximize_window()
# time.sleep(2)
#
#
# click_button_download_file = driver.find_element(By.XPATH, '//button[contains(text(), "Download File")]') # Создали кастомный путь с использованием текста
# click_button_download_file.click()
# print('File Download')

"""Директория не пустая, проверка"""
# if os.listdir(path_downloads):
#     print("File Yes")
# else:
#     print("File No")

"""Содержимое дериктории, проверка"""
# print(os.listdir(path_downloads))

"""Наличие требуемого файла в дериктории, проверка"""
# file_name = "Viking.jpg"
# file_path = path_downloads + '\\' + file_name
# assert os.access(file_path, os.F_OK) == True
# print("File OK")

"""Файл не пуст, проверка"""
# files = glob.glob(os.path.join(path_downloads, "*.*"))
# for file in files:
#     a = os.path.getsize(file)
#     if a > 10:
#         print("File Yes")
#     else:
#         print("File No")

"""Очистка дериктории"""
files = glob.glob(os.path.join(path_downloads, "*.*"))
for file in files:
    os.remove(file)




