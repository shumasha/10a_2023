a=int(input('Введите натуральное число:'))
def pr(a):
    k=1000
    while a>0:
        print('M'*(a//k))
        a=a%k
        k=k//10
        print('C'*(a//k))
        a=a%k
        k=k//10
        print('X'*(a//k))
        a=a%k
        k=k//10
        print('I'*(a//k))
pr(a)
 
