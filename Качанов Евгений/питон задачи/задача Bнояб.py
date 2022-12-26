def sum_chisel(k):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n // 10
    return n
n = map(int, input().split())
n = sum_chisel(n)
print(n)

       
