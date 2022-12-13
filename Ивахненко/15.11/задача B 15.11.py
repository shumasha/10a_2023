A=int(input('Введите натуральное число:'))
def numb(A):
    k=1000
    while A>0:
        print(A//k)
        A=A%k
        k=k//10
numb(A)
