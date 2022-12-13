print ("Введите первое число")
a = int(input())
print ("Введите второе число") 
b = int(input())
def Sum (a, b):
    while a != b:
        if a > b:
            a = a - b
        else: 
            b = b - a
    return b
print("Результат: ", Sum(a,b))



            
            
        
