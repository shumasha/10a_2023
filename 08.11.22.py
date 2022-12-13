from tkinter import *
root = Tk()
root.title('Задача29. Вариант №14)
nadp_A = Label(root, text = 'Введите сторону А', font = 'Arial 12')
nadp_B = Label(root, text = 'Введите сторону B', font = 'Arial 12')
nadp_C = Label(root, text = 'Результат C', font = 'Arial 12')
nadp_h= Label (root,text = 'Введие сторону h', font = 'Arial 12')
nadp_alpha= Label(root,text = 'Введие сторону alpha', font = 'Arial 12')
nadp_beta= Label(root,text = 'Введие сторону beta', font = 'Arial 12')
nadp_gamma= Label(root,text = 'Введие сторону gamma', font = 'Arial 12')
           
A=DoubleVar()
vA = Entry(root, width=15, textvariable = A)
B=DoubleVar()
vB = Entry(root, width=15, textvariable = B)
C=DoubleVar()
vC = Entry(root, width=15, textvariable = C)
h=DoubleVar()
vh = Entry(root, width=15, textvariable = h)
alpha=DoubleVar()
valpha = Entry(root, width=15, textvariable = alpha)
beta=DoubleVar()
vbeta = Entry(root, width=15, textvariable = beta)
gamma=DoubleVar()
vgamma = Entry(root, width=15, textvariable = gamma)

nadp_A.grid(row = 0, column = 0)
vA.grid(row = 0, column = 1)
nadp_B.grid(row = 1, column = 0)
vB.grid(row = 1, column =1)
nadp_C.grid(row = 2, column = 0)
vC.grid(row = 2, column =1)

knopka_raschet = Button(root, text = 'Расчет', width = 10)
knopka_vihod = Button(root, text = 'Выход', width = 10)
knopka_raschet.grid(row = 3, column = 0)
knopka_vihod.grid(row = 3, column = 1)



def Raschet(event):
    storA = A.get()
    storB = B.get()

    storC = storA+storB
    C.set('%.3f'% storC)
    

knopka_raschet.bind('<Button-1>', Raschet)

