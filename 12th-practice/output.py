from vektor import *

a = VektorInSpace(3, 4, 5)
b = VektorInSpace(5, 6, 7)

print(f'Длина вектора: {a.length()}')
print(f'Угловой коэффициент: {a.angle()}')
print(f'Сумма векторов: {a.sum(b)}')
print(f'Разность векторов: {a.diff(b)}')
print(f'Скалярное произведение векторов: {a.scalar(b)}')
print(f'Угол между xOy: {a.xOy()}')
print(f'Угол между xOz: {a.xOz()}')
print(f'Угол между yOz: {a.yOz()}')