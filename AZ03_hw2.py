# Построй диаграмму рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`.​
# import numpy as np
# random_array = np.random.rand(5) # массив из 5 случайных чисел
# print(random_array)

import numpy as np
import matplotlib.pyplot as plt

random_array_x = np.random.rand(5) # массив из 5 случайных чисел
print(random_array_x)
random_array_y = np.random.rand(5) # массив из 5 случайных чисел
print(random_array_y)

plt.scatter(random_array_x, random_array_y)

plt.xlabel('ось Х')
plt.ylabel('Ось Y')
plt.title('Диаграмма рассеивания случайных чисел')

plt.show()

