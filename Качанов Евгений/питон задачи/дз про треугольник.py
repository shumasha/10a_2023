from tkinter import*
import math
root = Tk()
root.title('Задача 29, вариант 4')
root.geometry('600x500')
#Создание надписей
h = Label(root,text = 'введите высоту треугольника')
с = Label(root,text = 'введите сторону треугольника')
b = Label(root,text = 'введите вторую сторону треугольника')
S = Label(root,text = 'площадь равна:')
a = Label(root,text = 'третяя сторона равна:')
yA = Label(root,text = 'угол а равен:')
yB = Label(root,text = 'угол б равен:')
yC = Label(root,text = 'угол с равен:')
P = Label(root,text = 'периметр равен:')
#Создание полей
h_1 = DoubleVar()
visota = Entry(root, width = 10, textvariable = h_1)
с_2 = DoubleVar()
storona_1 = Entry(root, width = 10, textvariable = с_2)
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
ygol_3  = Entry(root, width = 10, textvariable = yC_8)
P_9 = DoubleVar()
perimetr = Entry(root, width = 10, textvariable = P_9)
#Размещаем в окне
h.grid(row = 0, column = 0)
с.grid(row = 1, column = 0)
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
storona_3.grid(row = 3, column = 1)
ploshad.grid(row = 4, column = 1)
ygol_1.grid(row = 5, column = 1)
ygol_2.grid(row = 6, column = 1)
ygol_3.grid(row = 7, column = 1)
perimetr.grid(row = 8, column = 1)
#кнопки и события
knopka_raschet = Button(root, text = 'Расчет', width = 10)
knopka_vihod = Button(root, text = 'Выход', width = 10)
knopka_raschet.grid(row = 9, column = 0)
knopka_vihod.grid(row = 9, column = 1)


def Rashet(event):
    storh = h_1.get()
    storc = с_2.get()
    storb = b_3.get()
#Рассчитываем
    storS = 0.5*storc*storh
    S_4.set('%.3f'% storS)
    c1 = math.sqrt(storb**2-storh**2)
    c2 = storc - c1 
    stora = math.sqrt(c2**2+storh**2)
    a_5.set('%.3f'% stora)
    cosA = storh/storb
    storyA = math.sqrt(storc**2+storb**2-2*storc*storb*cosA)
    yA_6.set('%.3f'% storyA)
    cosB = storb/stora
    storyB = math.sqrt(storc**2+stora**2-2*stora*storc*cosB)
    yB_7.set('%.3f'% storyB)
    storyC = 180 - (storyB+storyA)
    yC_8.set('%.3f'% storyC)
    storP = math.sqrt(storb**2+storc**2-2*storb*storc*cosA)+storb+storc
    P_9.set('%.3f'% storP)

#Событие
knopka_raschet.bind('<Button-1>', Rashet)
#import math 
#S = 0.5*c*h
#c1 = math.sqrt(b**2-h**2)
#c2 = c - c1 
#a = math.sqrt(c2**2+h**2)
#cosA = h/b
#yA = math.sqrt(c**2+b**2-2*c*b*cosA)
#cosB = h/a
#yB = math.sqrt(c**2+a**2-2*a*c*cosB)
#yC = 180 - (yB+yA)
#P = math.sqrt(b**2+c**2-2*b*c*cosA)+b+c
#print(S, a, yA, yB, yC, P)
