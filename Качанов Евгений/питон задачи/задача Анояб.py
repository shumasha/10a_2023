def naib_del(a, b):
    while  a != b:
        if a > b:
            a -= b
            
        else:
            print('первое число должно быть больше второго')
        break
    return a
a, b = map(int, input().split())
n = naib_del(a, b)
print(n)
