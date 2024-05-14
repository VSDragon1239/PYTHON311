# Ваши данные
x = [3, 5, 7, 9, 11, 13]
y = [26, 76, 150, 240, 360, 500]

# Вычисление средних значений
mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

# Вычисление числителя и знаменателя для коэффициента b1
numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
denominator = sum((xi - mean_x)**2 for xi in x)

# Вычисление коэффициентов
b1 = numerator / denominator
b0 = mean_y - b1 * mean_x

print(f"Уравнение регрессии: Y = {b0} + {b1}X")
