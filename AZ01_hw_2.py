# Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv

import pandas as pd

df = pd.read_csv('dz.csv')

print(df)

df.dropna(inplace=True)
print(df)

group = df.groupby('City')['Salary'].mean()
print(group)