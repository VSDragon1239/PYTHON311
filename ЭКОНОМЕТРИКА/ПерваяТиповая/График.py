import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # Или 'Qt5Agg'


# Ваши данные
x = np.array([3, 5, 7, 9, 11, 13])
y = np.array([26, 76, 150, 240, 360, 500])

# Применение МНК для линейной регрессии (полином первого порядка)
coefficients = np.polyfit(x, y, 1)

# Коэффициенты линейной регрессии
b1, b0 = coefficients

# Создание последовательности значений x для линии регрессии
x_line = np.linspace(min(x), max(x), 100)

# Вычисление соответствующих значений y для линии регрессии
y_line = b0 + b1 * x_line

# Создание графика
plt.figure(figsize=(8, 6))

# Добавление точек данных на график
plt.scatter(x, y, color='blue', label='Data points')

# Добавление линии регрессии на график
plt.plot(x_line, y_line, color='red', label='Regression line')

# Добавление легенды
plt.legend()

# Показ графика
plt.show()
