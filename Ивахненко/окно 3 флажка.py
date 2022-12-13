import tkinter
from tkinter import*
root=Tk("окно")
root.title("заголовок")
root.geometry("500x400+300+200")
nadp=Label(root,text="ниже три флажка",font="Arial 18")
nadp.pack()
flag1=Checkbutton(root,text="1  ф л а ж о к",onvalue=1,offvalue=0)
flag1.pack()
flag2=Checkbutton(root,text="2  ф л а ж о к",onvalue=1,offvalue=0)
flag2.pack()
flag3=Checkbutton(root,text="3  ф л а ж о к",onvalue=1,offvalue=0)
flag3.pack()
