import tkinter
from tkinter import*
root=Tk("окно")
root.title("заголовок")
root.geometry("500x400+300+200")
nadp=Label(root,text="характеристики шрифта",font="Arial 18")
nadp.pack()
knopka_raschet=Button(root,text="расчёт")
knopka_raschet.pack()
pole=Entry(root,width=20)
pole.pack()
fl_grin=Checkbutton(root,text="П о л у ж и р н ы й ш р и ф т",onvalue=1,offvalue=0)
fl_grin.pack()
fl_kursiv=Checkbutton(root,text="К у р с и в",onvalue=1,offvalue=0)
fl_kursiv.pack()
