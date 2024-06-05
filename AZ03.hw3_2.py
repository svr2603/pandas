import pandas as pd
import matplotlib.pyplot as plt

# Загрузите CSV файл в DataFrame
df = pd.read_csv('prices_cleaned.csv')

plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=30, edgecolor='black')
plt.title('Гистограмма цен')
plt.xlabel('Цена (в рублях)')
plt.ylabel('Количество')

plt.show()