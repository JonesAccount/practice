from tkinter import *
from random import choice

window = Tk()

window.title("My first GUI")
window.config(background="gray")
window.iconbitmap("g.jpg")

window.geometry("500x500")
window.resizable(1, 0)


entry = Entry(window)
entry.pack()


def edit():
    entry.delete(0, len(entry.get()))
    entry.pack()


btn = Button(window,
             text="Очистить",
             bg="gray",
             fg="black",
             command=edit
             )
btn.pack()

window.mainloop()