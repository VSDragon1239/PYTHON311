import numpy as np
from scipy.optimize import curve_fit

# Ваши данные
x = np.array([289, 334, 300, 343, 356, 289, 341, 327, 357, 352, 381])  # Среднемесячная начисленная заработная плата
y = np.array([6.9, 8.7, 6.4, 8.4, 6.1, 9.4, 11.0, 6.4, 9.3, 8.2, 8.6])  # Доля денежных доходов


# Линейное уравнение
def linear(x, a, b):
    return a * x + b


popt, _ = curve_fit(linear, x, y)
a, b = popt
print(f'Линейное уравнение: y = {a}x + {b}')


# Степенное уравнение
def power(x, a, b):
    return a * np.power(x, b)


popt, _ = curve_fit(power, x, y)
a, b = popt
print(f'Степенное уравнение: y = {a}x^{b}')


# Экспоненциальное уравнение
def exponential(x, a, b):
    return a * np.exp(b * x)


popt, _ = curve_fit(exponential, x, y)
a, b = popt
print(f'Экспоненциальное уравнение: y = {a}e^{b}x')
