import numpy as np

# Исходные данные
x = np.array([78, 82, 87, 79, 89, 106, 67, 88, 73, 87, 76, 115])
y = np.array([133, 148, 134, 154, 162, 195, 139, 158, 152, 162, 159, 173])

# Количество наблюдений
n = len(x)

# Расчет сумм
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x2 = np.sum(x**2)
sum_xy = np.sum(x*y)

# Расчет параметров модели
a = (sum_y * sum_x2 - sum_x * sum_xy) / (n * sum_x2 - sum_x**2)
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)

print(f"Параметры модели: theta_0 = {a}, theta_1 = {b} \n")

f_y = a + b * x

print(f"значения x по y: {f_y}")

# Расчет относительной ошибки аппроксимации
A = np.abs((y - f_y) / y) * 100

print(f"Относительная ошибка аппроксимации A_i: {A}")
