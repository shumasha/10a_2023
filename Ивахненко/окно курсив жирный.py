import tkinter
from tkinter import*
root=Tk("окно")
root.title("заголовок")
root.geometry("500x400+300+200")
nadp=Label(root,text="характеристики шрифта",font="Arial 18")
nadp.pack()
of_girn=Checkbutton(root,text="П о л у ж и р н ы й",onvalue=1,offvalue=0)
of_girn.pack()
of_kursiv=Checkbutton(root,text="К у р с и в",onvalue=1,offvalue=0)
of_kursiv.pack()
