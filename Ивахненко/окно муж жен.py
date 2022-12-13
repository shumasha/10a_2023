import tkinter
from tkinter import*
root=Tk("окно")
root.title("заголовок")
root.geometry("500x400+300+200")
nadp=Label(root,text="кто вы?",font="Arial 18")
nadp.pack()
per1=Radiobutton(root,text="М у ж ч и н а",value=1)
per1.pack()
per2=Radiobutton(root,text="Ж е н щ и н а",value=2)
per2.pack()
