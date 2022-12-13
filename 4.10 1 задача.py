import math
R1=int(input("введите сопротивление"))
R2=int(input("введите сопротивление"))
R3=int(input("введите сопротивление"))
R=R1*R2*R3/(R1*R2+R1*R3+R2*R3)
print("R=",R)
