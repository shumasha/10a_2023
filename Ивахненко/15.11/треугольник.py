import tkinter
from tkinter import *
root=Tk()
root.title('Задача 29. Вариант 15')
nadp_A=Label(root, text='a', font='Arial 18')
nadp_B=Label(root, text='b', font='Arial 18')
nadp_C=Label(root, text='c', font='Arial 18')
nadp_alpha=Label(root, text='alpha', font='Arial 18')
nadp_beta=Label(root, text='beta', font='Arial 18')
nadp_gamma=Label(root, text='gamma', font='Arial 18')
nadp_h=Label(root, text='h', font='Arial 18')
nadp_S=Label(root, text='S', font='Arial 18')
nadp_P=Label(root, text='P', font='Arial 18')
nadp_A.grid(row=0, column=0)
nadp_B.grid(row=1, column=0)
nadp_C.grid(row=2, column=0)
nadp_alpha.grid(row=3, column=0)
nadp_beta.grid(row=4, column=0)
nadp_gamma.grid(row=5, column=0)
nadp_h.grid(row=6, column=0)
nadp_S.grid(row=7, column=0)
nadp_P.grid(row=8, column=0)

A=DoubleVar()
vvod_A=Entry(root, width=10, textvariable=A)
B=DoubleVar()
vvod_B=Entry(root, width=10, textvariable=B)
C=DoubleVar()
vvod_C=Entry(root, width=10, textvariable=C)
d=DoubleVar()
vvod_alpha=Entry(root, width=10, textvariable=d)
f=DoubleVar()
vvod_beta=Entry(root, width=10, textvariable=f)
g=DoubleVar()
vvod_gamma=Entry(root, width=10, textvariable=g)
h=DoubleVar()
vvod_h=Entry(root, width=10, textvariable=h)
S=DoubleVar()
vvod_S=Entry(root, width=10, textvariable=S)
P=DoubleVar()
vvod_P=Entry(root, width=10, textvariable=P)

vvod_A.grid(row=0, column=1)
vvod_B.grid(row=1, column=1)
vvod_C.grid(row=2, column=1)
vvod_alpha.grid(row=3, column=1)
vvod_beta.grid(row=4, column=1)
vvod_gamma.grid(row=5, column=1)
vvod_h.grid(row=6, column=1)
vvod_S.grid(row=7, column=1)
vvod_P.grid(row=8, column=1)

raschet=Button(root, text='Расчет', width=10)
vihod=Button(root, text='Выход', width=10)
raschet.grid(row=9, column=0)
vihod.grid(row=9, column=1)

def ras(event):
    stor_h=h.get()
    stor_A=A.get()
    stor_b=f.get()

    stor_g=stor_b
    g.set('%.3f'% stor_g)
    if stor_g+stor_b<180:
        stor_d=180-stor_g-stor_b
        d.set('%.3f'% stor_d)
    
def vih(event):
    root.destroy()

raschet.bind('<Button-1>', ras)
vihod.bind('<Button-2>', vih)


