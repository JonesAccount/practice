from tkinter import *
from random import choice

window = Tk()

window.title("My first GUI")
window.config(background="gray")
window.iconbitmap("g.jpg")

window.geometry("500x500")
window.resizable(1, 0)


t = Text(window)
t.pack()

def func():
    window.destroy()

def func2():
    print(t.get(1.2))
    print(t.get(2.0, 5.0))
    e.insert(0, t.get(3.3))
    t.insert(END, "Hello")
    t.insert(END, " world!")

def func3():
    e.delete(0, END)
    t.delete(1.0, END)



b = Button(window, text="exit", command=func)
b.pack()

b2 = Button(window, text="Click", command=func2)
b2.pack()

b3 = Button(window, text="delete", command=func3)
b3.pack()

e = Entry(window)
e.pack()


window.mainloop()