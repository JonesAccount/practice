from tkinter import *
from random import randint

window = Tk()

# ----------Page----------
window.title("Поймай если сможешь!")
window.config(bg="black")
window.geometry("300x300")
window.resizable(0, 0)


# ----------Function----------
def enter(event):
    frm.place(x=randint(0, 270), y=randint(0, 270))


# ----------Frame----------
frm = Frame(master=window, bg="black", relief=FLAT, width=30, height=30)


# ----------Text----------
lbl = Label(master=frm, text="⌾", font=("Arial", 40), fg="white", bg="black")


# ----------Event----------
frm.bind("<Enter>", enter)


# ----------Show widget----------
frm.place(x=randint(0, 270), y=randint(0, 270))
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)


window.mainloop()