import tkinter
from tkinter import*
root=Tk("окно")
root.title("заголовок")
root.geometry("500x400+300+200")
nadp=Label(root,text="ниже три переключателя(радио кнопки)",font="Arial 18")
nadp.pack()
flag1=Radiobutton(root,text="п е р в а я",value=1)
flag1.pack()
flag2=Radiobutton(root,text="в т о р а я",value=2)
flag2.pack()
flag3=Radiobutton(root,text="т р е т ь я",value=3)
flag3.pack()
ramka1=Frame(root,width=500,height=100)
ramka1.pack()
ramka1 = Frame(root,width=500,height=100,bg="darkred")
ramka1.pack()
