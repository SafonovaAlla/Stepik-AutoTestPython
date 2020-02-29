from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# 1.	Изменение языка интерфейса c русского на польский
# 1.1.	зайти на адрес http://selenium1py.pythonanywhere.com/ru/.
browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/")
time.sleep(5)
# 1.2.	изменить в выпадающем меню (слева сверху) язык с русского на polski
select = Select(browser.find_element_by_name("language"))
select.select_by_value("pl")  # ищем элемент с текстом "polski"
# 1.3.	нажать кнопку «Выбрать»
choice = browser.find_element_by_css_selector("form#language_selector button")
choice.click()
# 1.4.	дождаться перехода на адрес http://selenium1py.pythonanywhere.com/pl/
# 1.5.	тест успешно завершен, если на загруженной странице текст кнопки выбора языка соответствует строке «Wykonaj»
choice = browser.find_element_by_css_selector("form#language_selector button")
assert "Wykonaj" in choice.text
print("\r\nassertion 1 ok\r\n")

time.sleep(4)
browser.close()

# 4.	Цена добавленного товара прибавляется к сумме на значке корзины
# 4.1.	зайти на адрес каталога магазина
browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/")
# узнасть стоимость первого товара (взять в переменную число в поле цена первой карточки товара)
x_element = browser.find_element_by_css_selector("ol.row li:nth-child(1) p.price_color")
x = x_element.text
x = x.replace(",", ".")
x = x.replace(" £", "")
x = float(x)

# 4.2.	добавить в корзину первый товар (нажать на кнопку в первой карточке товара)
button = browser.find_element_by_css_selector("ol.row li:nth-child(1) button")
button.click()

# 4.3.	Тест пройден успешно, если изменилась сумма в графе «всего в корзине», увеличившись на цену добавленного товара)
y_element = browser.find_element_by_css_selector("div.alertinner p strong")
y = y_element.text
y = y.replace(",", ".")
y = y.replace(" £", "")
y = float(y)

assert x == y
print("\r\nassertion 4 ok\r\n")

time.sleep(4)
browser.close()