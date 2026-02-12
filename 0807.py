from tkinter import *
from random import choice

window = Tk()

window.title("My first GUI")
window.config(background="gray")
window.iconbitmap("g.jpg")

window.geometry("500x500")
window.resizable(1, 0)



colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]

label = Label(window,
              text="red, green, blue, yellow, cyan, magenta",
              font=("Arial", 10, "bold"),
              bg="gray"
              )
label.pack()

entry = Entry(window)
entry.pack()

def edit():
    if entry.get() == "1":
        window.config(background="red")
    elif entry.get() == "2":
        window.config(background="green")
    elif entry.get() == "3":
        window.config(background="blue")
    elif entry.get() == "4":
        window.config(background="yellow")
    elif entry.get() == "5":
        window.config(background="cyan")
    elif entry.get() == "6":
        window.config(background="magenta")

def edit2():
    lb = Label(window,
               text="нОвый текст",
               font=("Arial", 10, "bold"))
    lb.pack()

btn = Button(window,
             text="Изменить фон",
             command=edit,
             bg="gray",
             fg="black"
             )
btn.pack()
btn2 = Button(window,
             text="Изменить текст",
             command=edit2,
             bg="gray",
             fg="black"
             )
btn2.pack()

window.mainloop()