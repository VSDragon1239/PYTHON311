import matplotlib.pyplot as plt

# Данные
x = [78, 82, 87, 79, 89, 106, 67, 88, 73, 87, 76, 115]
y = [133, 148, 134, 154, 162, 195, 139, 158, 152, 162, 159, 173]

# Шаг 1: Построение диаграммы рассеяния
plt.figure(figsize=(8, 6))
plt.scatter(x, y)
plt.title('Диаграмма рассеяния')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
