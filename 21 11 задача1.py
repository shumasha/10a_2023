num = int(input("ВВедите целое число: "))
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print("Сумма числ равна: ", sum)    
