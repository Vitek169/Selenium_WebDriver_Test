import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url) #переходим по ссылке
driver.maximize_window() #переводим в полноэкракнный режим

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

"""Выбираем сортировку товара по цене от меньшей к большей"""
menu_sort = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select')
menu_sort.click()
time.sleep(1)
print('Click Menu Sorting')
menu_sort.send_keys(Keys.DOWN)
menu_sort.send_keys(Keys.DOWN)
menu_sort.send_keys(Keys.DOWN)
menu_sort.click()
print('Soring Price Low -> High Is Good')
time.sleep(1)

"""Информация о первом товаре"""
sauce_labs_fleece_jacket = driver.find_element(By.XPATH, '//a[@id = "item_5_title_link"]')
value_sauce_labs_fleece_jacket = sauce_labs_fleece_jacket.text #Информация о названии
print(value_sauce_labs_fleece_jacket)

price_sauce_labs_fleece_jacket = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_sauce_labs_fleece_jacket = price_sauce_labs_fleece_jacket.text #Информация о цене
print(value_price_sauce_labs_fleece_jacket)
"""Нажимаем кнопку добавления в корзину первого товара"""
sauce_labs_fleece_jacket_add = driver.find_element(By.XPATH, '//button[@id = "add-to-cart-sauce-labs-fleece-jacket"]')
sauce_labs_fleece_jacket_add.click()
print('First Product Add')
time.sleep(1)

"""Скролим страницу вниз"""
driver.execute_script('window.scroll(0, 1000)')
print('Scroll Page Down')
time.sleep(1)

"""Информация о втором товаре"""
sauce_labs_onesie = driver.find_element(By.XPATH, '//a[@id = "item_2_title_link"]')
value_sauce_labs_onesie = sauce_labs_onesie.text #Информация о названии
print(value_sauce_labs_onesie)

price_sauce_labs_onesie = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div')
value_price_sauce_labs_onesie = price_sauce_labs_onesie.text #Информация о цене
print(value_price_sauce_labs_onesie)
"""Нажимаем кнопку добавления в корзину второго товара"""
sauce_labs_onesie_add = driver.find_element(By.XPATH, '//button[@id = "add-to-cart-sauce-labs-onesie"]')
sauce_labs_onesie_add.click()
print('Second Product Add')
time.sleep(1)

"""Скролим страницу вверх вверх"""
driver.execute_script('window.scroll(0, -1000)')
print('Scroll Page Up')
time.sleep(1)
"""Переходим в корзину"""
shoping_cart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
shoping_cart_button.click()
print('Enter In Card')
time.sleep(1)

"""Проверяем, что указанные товары в карзине соответсвуют тем, которые мы выбрали"""

"""Продукт первый"""
cart_sauce_labs_fleece_jacket = driver.find_element(By.XPATH, '//a[@id = "item_5_title_link"]')
value_cart_sauce_labs_fleece_jacket = cart_sauce_labs_fleece_jacket.text
print(value_cart_sauce_labs_fleece_jacket)
assert value_sauce_labs_fleece_jacket == value_cart_sauce_labs_fleece_jacket
print('First Product Is Good')

cart_price_sauce_labs_fleece_jacket = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_cart_price_sauce_labs_fleece_jacket = cart_price_sauce_labs_fleece_jacket.text
print(value_cart_price_sauce_labs_fleece_jacket)
assert value_cart_price_sauce_labs_fleece_jacket == value_price_sauce_labs_fleece_jacket
print('Price First Product is Good')

"""Продукт второй"""
cart_sauce_labs_onesie = driver.find_element(By.XPATH, '//a[@id = "item_2_title_link"]')
value_cart_sauce_labs_onesie = cart_sauce_labs_onesie.text
print(value_cart_sauce_labs_onesie)
assert value_sauce_labs_onesie == value_cart_sauce_labs_onesie
print('First Product Is Good')

cart_price_sauce_labs_onesie= driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_cart_price_sauce_labs_onesie = cart_price_sauce_labs_onesie.text
print(value_cart_price_sauce_labs_onesie)
assert value_cart_price_sauce_labs_onesie == value_price_sauce_labs_onesie
print('Price Second Product is Good')

"""Нажимаем на кнопку для оформления покупки"""
checkout_button = driver.find_element(By.XPATH, '//button[@id = "checkout"]')
checkout_button.click()
print('Click Checkout Button')
checkout_info = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
value_checkout_info = checkout_info.text
print(f'{value_checkout_info}. Is Good!')


"""Вводим данные в поля"""
first_name_input = driver.find_element(By.XPATH, '//input[@id = "first-name"]')
first_name_input.send_keys('Viktor')
print('Enter First Name')
time.sleep(1)
last_name_input = driver.find_element(By.XPATH, '//input[@id = "last-name"]')
last_name_input.send_keys('Matuizo')
print('Enter Last Name')
time.sleep(1)
zip_cod_input = driver.find_element(By.XPATH, '//input[@id = "postal-code"]')
zip_cod_input.send_keys('Ukhta')
print('Enter Zip Cod')
time.sleep(1)

"""Нажимаем кнопку Continue"""
button_continue = driver.find_element(By.XPATH, '//input[@id = "continue"]')
button_continue.click()
print('Click Continue Button')
time.sleep(1)

"""Проверяем, что прордукты к оплате соответствуют продуктам, которые откладывали"""

"""Продукт первый"""
ordere_sauce_labs_fleece_jacket = driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]/div')
value_ordere_sauce_labs_fleece_jacket = ordere_sauce_labs_fleece_jacket.text
print(value_ordere_sauce_labs_fleece_jacket)
assert value_sauce_labs_fleece_jacket == value_ordere_sauce_labs_fleece_jacket
print('First Product Is Good')

order_price_sauce_labs_fleece_jacket = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_order_price_sauce_labs_fleece_jacket = order_price_sauce_labs_fleece_jacket.text
print(value_order_price_sauce_labs_fleece_jacket)
assert value_order_price_sauce_labs_fleece_jacket == value_price_sauce_labs_fleece_jacket
print('Price First Product is Good')

"""Продукт второй"""
order_sauce_labs_onesie = driver.find_element(By.XPATH, '//a[@id = "item_2_title_link"]')
value_order_sauce_labs_onesie = order_sauce_labs_onesie.text
print(value_order_sauce_labs_onesie)
assert value_sauce_labs_onesie == value_order_sauce_labs_onesie
print('First Product Is Good')

order_price_sauce_labs_onesie = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_order_price_sauce_labs_onesie = order_price_sauce_labs_onesie.text
print(value_order_price_sauce_labs_onesie)
assert value_order_price_sauce_labs_onesie == value_price_sauce_labs_onesie
print('Price Second Product is Good')

"""Сравниваем сумму двух товаров с финальной ценой"""
item_total = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[5]')
value_item_total = item_total.text
sum_value_item_total = value_item_total.replace('Item total: $', '')
print(f'{sum_value_item_total} Убираем Item total: $ в тексте')

price_product_1 = value_cart_price_sauce_labs_fleece_jacket.replace('$', '')
price_product_2 = value_cart_price_sauce_labs_onesie.replace('$', '')
sum_product = float(price_product_1) + float(price_product_2)
print(f'{sum_product}. Сумма обоих продуктов без знака $.')
assert str(sum_product) == sum_value_item_total
print('Item Total = Summ in Card!')



"""Скролим страницу вниз"""
driver.execute_script('window.scroll(0, 1000)')
print('Scroll Page Down')

"""Нажимаем кнопку Finish"""
button_finish = driver.find_element(By.XPATH, '//button[@id = "finish"]')
button_finish.click()
print('Click Button Finish')
time.sleep(1)

"""Проверяем переход на конечную страницу после оплаты товаров"""
finish_text = driver.find_element(By.XPATH, '//*[@id= "checkout_complete_container"]/h2')
print(finish_text.text)

"""Переходим на домашнюю страницу"""
button_back_home = driver.find_element(By.XPATH, '//button[@id = "back-to-products"]')
button_back_home.click()
print('Back Home Page')

"""Проверяем переход на домашнюю страницу"""
print(f'{value_string_products}. Back Home!')
print('ТЕСТ ОКОНЧЕН')



