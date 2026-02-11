from asyncio import get_event_loop
from tkinter import *
from random import choice
from time import sleep as sl

from pygments.styles.dracula import background

root = Tk()

root.title("Первая программа 😃")
root.iconbitmap("photo.png")
root.config(bg="green")

root.geometry("900x600")
root.resizable(0, 0)

colors = ["yellow", "red", "black", "purple", "green", "gray", "blue", "orange"]


def click(word: str = "Приветик!"):
    root.config(bg=choice(colors))
    print(word)




btn1 = Button(root,
              text="Нажми!",
              font="Arial 40 bold",
              width=10,
              height=5,
              fg="red",
              background="green",
              activebackground="yellow",
              activeforeground="purple",
              command=click
             )

btn2 = Button(root,
              text="Кнопка вторая",
              font=("Comic Sans MS", 30, "bold"),
              width=15,
              height=5,
              bg="yellow"
            )

def tex():
    global btn2


btn3 = Button(root,
              text="Это уже третяя кнопка",
              font=("Comic Sans MS", 25, "italic"),
              width=20,
              height=5,
              command=tex
            )


btn1.pack(); btn2.pack(); btn3.pack()


root.mainloop()


# def click2():
#     while True:
#         root.config(bg=choice(colors))
#         sl(1)

# btn2 = Button(root, text="Дискотека!", command=click2)
# btn2.pack()




"""
Классы
Button -> text, command, font, width, height, bg, activatebackground, fg

Методы
pack
"""