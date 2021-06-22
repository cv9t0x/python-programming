from vektor import Vektor

# Присваивание координат двух векторов (x1, y1, x2, y2)
a = Vektor(2, 3)
b = Vektor(3, 4)

# Вывод
print(f'Длина вектора: {a.length()}')
print(f'Угловой коэффициент: {a.angle()}')
print(f'Сумма векторов: {a.sum(b)}')
print(f'Разность векторов: {a.diff(b)}')
print(f'Скалярное произведение векторов: {a.scalar(b)}')