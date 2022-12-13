import tkinter
from tkinter import*
root=Tk("Окно")
root.title("Заголовок")
root.geometry("500x400+300+200")
ramka=Frame(root)
ramka.pack()
knopka1=Button(ramka, text='Кнопка1')
knopka1.grid(row = 0, column = 0)
knopka2=Button(ramka, text='Кнопка2')
knopka2.grid(row = 0, column = 1)
knopka3=Button(ramka, text='Кнопка3')
knopka3.grid(row = 1, column = 0)
