import math
print('Введите параметры координат на плоскости')
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
a = y1 - y2
b = x1 - x2
c = math.sqrt (a**2+b**2)
print('Расстояние между точками равно:', c)
