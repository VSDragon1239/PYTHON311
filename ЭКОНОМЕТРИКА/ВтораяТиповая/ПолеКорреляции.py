import numpy as np

# Ваши данные
x = np.array([554, 560, 545, 672, 796, 777, 632, 688, 833, 577, 584, 949, 888, 831, 562, 665, 705])
y = np.array([302, 160, 310, 415, 452, 502, 355, 416, 501, 403, 208, 462, 368, 399, 342, 354, 558])


# Вычисляем средние значения
x_mean = np.mean(x)
y_mean = np.mean(y)

# Вычисляем числитель и знаменатель для коэффициента корреляции Пирсона
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))

# Вычисляем коэффициент корреляции Пирсона
r_xy = numerator / denominator

print(f"Коэффициент корреляции Пирсона: {r_xy}")
print(x_mean, y_mean)

