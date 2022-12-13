p=(int(input('Ввод основания системы:'))
N10=(int(input('Ввод исходного 10-тичного числа:'))
k=1
Np=0
  while True:
   Np=Np+(N10%p)*k
   k=k*10
   N10=N10//p
  if (N10=0): break
print('N', p, '=', Np)
   
   
