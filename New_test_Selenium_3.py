import datetime
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
faker = Faker('ru_RU')

base_url = 'https://www.saucedemo.com/'
driver.get(base_url) #переходим по ссылке
# driver.maximize_window() #переводим в полноэкракнный режим



class Test_Selenium_3:

    def __init__(self):
        pass


    def login(self):
        """Логинимся на сайте путем ввода Username и Password"""
        username_input = driver.find_element(By.XPATH, '//input[@id = "user-name"]')
        username_input.send_keys('standard_user')
        print('Enter Username')
        time.sleep(1)

        password_input = driver.find_element(By.XPATH, '//input[@id = "password"]')
        password_input.send_keys('secret_sauce')
        print('Enter password')
        time.sleep(1)

        button_login = driver.find_element(By.XPATH, '//input[@id = "login-button"]')
        button_login.click()
        print('Press Button Login')
        time.sleep(1)

        """Проверяем успешно ли залогинились, введя правильные данные"""
        string_products = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
        value_string_products = string_products.text
        print(f'{value_string_products}. Authorization is GOOD!')

    def enter_product(self):
        """Создаю переменные с XPATH кнопок добавления товара"""
        backpack = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        bike_light = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
        bolt_t_shirt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        fleece_jacket = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
        onesie = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
        t_shirt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
        all_product = [backpack, bike_light, bolt_t_shirt, fleece_jacket, onesie, t_shirt]

        print("Приветствую тебя в нашем интернет - магазине")
        print("Выбери один из следующих товаров и укажи его номер: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light, 3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie, 6 - Test.allTheThings() T-Shirt (Red)")
        product = input('Введите цифру нужного товара: ')
        print(product)

        if product == '1':
            all_product[0].click()
            print('Товар 1 добавлен в корзину')

        if product == '2':
            all_product[1].click()
            print('Товар 2 добавлен в корзину')

        if product == '3':
            all_product[2].click()
            print('Товар 3 добавлен в корзину')

        if product == '4':
            all_product[3].click()
            print('Товар 4 добавлен в корзину')

        if product == '5':
            all_product[4].click()
            print('Товар 5 добавлен в корзину')

        if product == '6':
            all_product[5].click()
            print('Товар 6 добавлен в корзину')
        time.sleep(6)


    def check_product(self):
        """Создаю метод проверки товаров по назанию и цене"""
        Sauce_Labs_Backpack = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]/div')
        Value_Sauce_Labs_Backpack = Sauce_Labs_Backpack.text
        Sauce_Labs_Backpack_Payment = driver.find_element(By.XPATH, '//div[@class="inventory_item_price"]')
        Value_Sauce_Labs_Backpack_Payment = Sauce_Labs_Backpack_Payment.text
        print(f'Цена {Value_Sauce_Labs_Backpack} - {Value_Sauce_Labs_Backpack_Payment}')
        """Переходим в корзину"""
        shoping_cart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        shoping_cart_button.click()
        print('Enter In Card')
        Card_Sauce_Labs_Backpack = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
        Card_Sauce_Labs_Backpack_Paymant = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
        print(Card_Sauce_Labs_Backpack_Paymant.text)
        assert  Card_Sauce_Labs_Backpack.text == Value_Sauce_Labs_Backpack
        print(f'Товар корзине соответствует выбранному')
        """Переходим для оплаты товара"""
        checkout_button = driver.find_element(By.XPATH, '//*[@id="checkout"]')
        checkout_button.click()
        print('Перешли дя ввода данных заказчика')
        first_name_input = driver.find_element(By.XPATH, '//input[@id = "first-name"]')
        name = faker.first_name()
        first_name_input.send_keys(name)
        print(name)
        time.sleep(1)
        last_name_input = driver.find_element(By.XPATH, '//input[@id = "last-name"]')
        last_name =  faker.last_name()
        last_name_input.send_keys(last_name)
        print(last_name)
        time.sleep(1)
        zip_cod_input = driver.find_element(By.XPATH, '//input[@id = "postal-code"]')
        zip = faker.password()
        zip_cod_input.send_keys(zip)
        print(zip)
        time.sleep(1)
        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_button.click()
        print('Переход на страницу для оплаты')







tests = Test_Selenium_3()
tests.login()
tests.enter_product()
tests.check_product()











