# 1. Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`.
#
# # Параметры нормального распределения
# mean = 0       # Среднее значение
# std_dev = 1    # Стандартное отклонение
# num_samples = 1000  # Количество образцов
#
# # Генерация случайных чисел, распределенных по нормальному распределению
# data = np.random.normal(mean, std_dev, num_samples)

import numpy as np
import matplotlib.pyplot as plt

mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)
print(data)

plt.hist(data, bins=8)

plt.xlabel('числа')
plt.ylabel('количество чисел')
plt.title('гистограмма распределения чисел')

plt.show()

