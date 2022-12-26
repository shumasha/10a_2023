import math
def NOD(x,y):
    while x!=y:
        if x>y:
            x-=y
        else:
            y-=x
    return x
a = int(input("First number: "))
b = int(input("Second number: "))
print('NOD: ', (a/0, b/0)/NOD(a,b))
