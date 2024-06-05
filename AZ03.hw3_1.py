import pandas as pd

# Загрузите CSV файл в DataFrame
df = pd.read_csv('prices.csv')

# Предположим, что столбец называется 'Price'
# Удаляем '₽/мес.', 'руб.', пробелы и преобразуем в числовой тип данных
df['Price'] = df['Price'].str.replace('₽/мес.', '', regex=True)\
                         .str.replace('руб.', '', regex=True)\
                         .str.replace(' ', '', regex=True)\
                         .astype(float)

# Сохраняем изменения обратно в CSV файл
df.to_csv('prices_cleaned.csv', index=False)

print(df.head())  # Проверка первых строк