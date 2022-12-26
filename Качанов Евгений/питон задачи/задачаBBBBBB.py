def chislo(n):
    while n !=0:
        print(n % 10)
        n = n // 10
n = input('Введите натуральное число: ')
chislo(n)
