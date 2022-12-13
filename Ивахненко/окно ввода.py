import tkinter
from tkinter import*
root=Tk("окно")
root.title("заголовок")
root.geometry("500x400+300+200")
nadp=Label(root,text="ниже окно для ввода",font="Arial 18")
nadp.pack()
pole=Entry(root,width=20)
pole.pack()
