from tkinter import*
import math
root = Tk()
root.title('Задача 29, вариант 4')
root.geometry('600x500')
#Создание надписей
h = Label(root,text = 'введите высоту треугольника:        ')
c = Label(root,text = 'введите сторону треугольника:       ')
b = Label(root,text = 'введите вторую сторону треугольника:')
S = Label(root,text = 'площадь треугольника равна:         ')
a = Label(root,text = 'третяя сторона треугольника равна:  ')
yA = Label(root,text = 'угол a треугольника равен:         ')
yB = Label(root,text = 'угол b треугольника равен:         ')
yC = Label(root,text = 'угол c треугольника равен:         ')
P = Label(root,text = 'периметр треугольника равен:        ')
#Создание полей
h_1 = DoubleVar()
visota = Entry(root, width = 10, textvariable = h_1)
c_2 = DoubleVar()
storona_1 = Entry(root, width = 10, textvariable = c_2)
b_3 = DoubleVar()
storona_2 = Entry(root, width = 10, textvariable = b_3)
S_4 = DoubleVar()
ploshad = Entry(root, width = 10, textvariable = S_4)
a_5 = DoubleVar()
storona_3 = Entry(root, width = 10, textvariable = a_5)
yA_6 = DoubleVar()
ygol_1 = Entry(root, width = 10, textvariable = yA_6)
yB_7 = DoubleVar()
ygol_2 = Entry(root, width = 10, textvariable = yB_7)
yC_8 = DoubleVar()
ygol_3 = Entry(root, width = 10, textvariable = yC_8)
P_9 = DoubleVar()
perimetr = Entry(root, width = 10, textvariable = P_9)
#Размещаем в окне
h.grid(row = 0, column = 0)
c.grid(row = 1, column = 0)
b.grid(row = 2, column = 0)
S.grid(row = 3, column = 0)
a.grid(row = 4, column = 0)
yA.grid(row = 5, column = 0)
yB.grid(row = 6, column = 0)
yC.grid(row = 7, column = 0)
P.grid(row = 8, column = 0)
visota.grid(row = 0, column = 1)
storona_1.grid(row = 1, column = 1)
storona_2.grid(row = 2, column = 1)
ploshad.grid(row = 3, column = 1)
storona_3.grid(row = 4, column = 1)
ygol_1.grid(row = 5, column = 1)
ygol_2.grid(row = 6, column = 1)
ygol_3.grid(row = 7, column = 1)
perimetr.grid(row = 8, column = 1)
#кнопки и события
knopka_raschet = Button(root, text = 'Расчет', width = 10)
knopka_vihod = Button(root, text = 'Выход', width = 10)
knopka_raschet.grid(row = 9, column = 0)
knopka_vihod.grid(row = 9, column = 1)

def Raschet (event):
    storh = h.get()
    storc = c.get()
    storb = b.get()
#Рассчитываем
    storS = 0.5*c*h
    S.set('%.3'% storS)
    c1 = math.sqrt(b**2-h**2)
    c2 = c - c1
    stora = math.sqrt(c2**2+h**2)
    a.set('%.3'% stora)
    cosA = h/b
    storyA = math.sqrt(c**2+b**2-2*a*c*cosA)
    yA.set('%.3'% storA)
    storyB = math.sqrt(c**2+a**2-2*a*c*cosB)
    yB.set('%.3'% storB)
    storyC = 180 - (yB+yA)
    yC.set('%.3'% storC)
    storyP = math.sqrt(b**2+c**2-2*b*c*cosA)+b+c
    P.set('%.3'% storP)
    
    




    




    


