from tkinter import*
root = Tk()
root.title('root')
root.geometry('500x400+300+200')
Nadpis = Label(root, text = 'Кокоджамбо', font = 'Arial 25')
Nadpis.pack()
ramka = Frame(root)
knopka1 = Button(ramka, text = 'Кнопка 1')
knopka2 = Button(ramka, text = 'Кнопка 2')
ramka.pack()
knopka1.grid(row = 0, column = 0)
knopka2.grid(row = 0, column = 1)
knopka3 = Button(root, text  = 'Кнопка 3' )
knopka3.pack()

Pole = Entry(root, width = 20)
Pole.pack()
Flajki = Checkbutton(root, text = 'Знаешь ли ты',onvalue = 1, offvalue = 0)
Flajki.pack()
Flajki_1= Checkbutton(root, text = 'вдоль ночных дорог',onvalue = 1, offvalue = 0)
Flajki_1.pack()
per1 = Radiobutton(root, text = 'MEn', value = 1)
per1.pack()
per2 = Radiobutton(root, text = 'Women ahahaha', value = 2)
per2.pack()
ramka1 = Frame(root, width = 500, height = 100, bd = 'darkred')
ramka1.pack()
