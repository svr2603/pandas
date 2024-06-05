# необходимо спарсить цены на диваны с сайта divan.ru в csv файл,
# обработать данные, найти среднюю цену и вывести ее,
# а также сделать гистограмму цен на диваны

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import csv


# Инициализация драйвера
driver = webdriver.Firefox()

# URL страницы для парсинга
url = 'https://www.divan.ru/category/pramye-divany'

# Открываем страницу
driver.get(url)

# Даем время на загрузку страницы
time.sleep(5)

prices = driver.find_elements(By.CSS_SELECTOR, '.ui-LD-ZU.KIkOH')

# Создаем список для хранения извлеченных цен
price_list = []

# Извлекаем текстовые значения цен
for price in prices:
    price_list.append(price.text)

# Закрываем драйвер
driver.quit()

# Создаем DataFrame и сохраняем его в CSV файл
df = pd.DataFrame(price_list, columns=['Price'])
df.to_csv('prices.csv', index=False)

print("Цены успешно сохранены в файл prices.csv")