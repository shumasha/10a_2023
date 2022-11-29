def NOD(x,y):
while x!=y:
if x>y:
x-=y
else:
y-=x
return x
a = int(input("первый номер: "))
b = int(input("второй номер: "))
print('NOD: ', (a*b)/NOD(a,b))
