from tkinter import *
from random import choice

window = Tk()

window.title("My first GUI")
window.config(background="gray")
window.iconbitmap("g.jpg")

window.geometry("500x500")
window.resizable(1, 0)


entry = Entry(window)
entry.insert(2, "сюда пиши текст")
entry.pack()


def edit1():
    entry.delete(0, END)
    entry.pack()

def edit2():
    entry.delete(0)
    entry.pack()

def edit3():
    entry.delete(len(entry.get()) - 1)
    entry.pack()

btn1 = Button(window,
             text="Удалить все",
             bg="gray",
             fg="black",
             command=edit1
             )
btn1.pack()

btn2 = Button(window,
             text="Удалить первый символ",
             bg="gray",
             fg="black",
             command=edit2
             )
btn2.pack()

btn3 = Button(window,
             text="Удалить второй символ",
             bg="gray",
             fg="black",
             command=edit3
             )
btn3.pack()

window.mainloop()