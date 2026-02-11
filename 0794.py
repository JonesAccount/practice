from tkinter import *
from random import randint

from markdown_it.presets import gfm_like

root = Tk()

root.title("Test")
root.iconbitmap("")
root.config(background="gray")

root.geometry("500x500")
root.resizable(0, 0)

def edit():
    root.title(randint(1, 10))

def editbut():
    global btn2
    btn2 = Button(root, text="1")
    return btn2.pack()

btn1 = Button(root,
              text="Менять название программы",
              font=("Arial", 20, "bold"),
              command=edit
              )

btn2 = Button(root,
              text="Изменить текст кнопки",
              font=("Sans Serif", 20, "italic"),
              command=editbut
              )

btn1.pack(); btn2.pack()

root.mainloop()