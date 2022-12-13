p=int(input('Ввод основания системы:'))
Np=int(input('Ввод исходного р-ричного числа:'))
k=1
N10=0
while Np!=0:
    N10=N10+(Np%10)*k
    k=k*p
    Np=Np//10
print('N10=', N10)

