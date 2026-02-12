from tkinter import *

window = Tk()

window.title("My first GUI")
window.config(background="gray")
window.iconbitmap("g.jpg")

window.geometry("500x500")
window.resizable(1, 0)

entry = Entry(window)
entry.pack()

def save():
    save = entry.get()
    print(save)

btn = Button(window,
             text="Click me",
             command=save
             )
btn.pack()

window.mainloop()