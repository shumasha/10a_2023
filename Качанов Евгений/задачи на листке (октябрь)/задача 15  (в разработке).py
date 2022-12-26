import math
def ploshad(x1, y1, x2, y2, x3, y3):
    a = ((x1-x2)**2 + (y1-y2)**2)**0.5
    b = ((x1-x3)**2 + (y1-y3)**2)**0.5
    c = ((x3-x2)**2 + (y3-y2)**2)**0.5
    P = a+b+c
    return P
n = ploshad(x1, y1, x2, y2, x3, y3)
print (n)
def perimetr(x1, y1, x2, y2, x3, y3):
    a = ((x1-x2)**2 + (y1-y2)**2)**0.5
    b = ((x1-x3)**2 + (y1-y3)**2)**0.5
    c = ((x3-x2)**2 + (y3-y2)**2)**0.5
    S = math.sqrt(P*(P-a)*(P-b)*(P-c))
    return S
k = perimetr(x1, y1, x2, y2, x3, y3)
print (k)


print('Введите параметры координат на плоскости: ')
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

