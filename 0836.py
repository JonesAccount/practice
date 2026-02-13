from tkinter import *

window = Tk()

# ----------Page----------
window.title("КНБ")
window.config(bg="black")
window.geometry("800x600")
window.resizable(0, 0)


# ----------Variable----------


# ----------Function----------


# ----------Frame----------
frm_title_game = Frame(
    master=window,
    bg="#575d7a",
    width=800,
    height=100,
    relief=RIDGE,
    bd=10)

frm_robot = Frame(
    master=window,
    bg="#575d7a",
    width=400,
    height=500,
    relief=RIDGE,
    bd=10)

frm_player = Frame(
    master=window,
    bg="#575d7a",
    width=400,
    height=500,
    relief = RIDGE,
    bd = 10)


# ----------Label----------
lbl_title_robot = Label(
    master=frm_robot,
    text="РОБОТ",
    font=("Comic Sans MS", 40, "bold"),
    bg="#575d7a",
    fg="white")

lbl_title_plaver = Label(
    master=frm_player,
    text="ИГРОК",
    font=("Comic Sans MS", 40, "bold"),
    bg="#575d7a",
    fg="white")


# ----------Entry----------


# ----------Text----------


# ----------Button----------
btn_stoun = Button(
    master=frm_player,
    text="Камень",
    font=("Comic Sans MS", 40, "bold"),
    bg="#575d7a",
    fg="white",
    width=7,
    height=1)

btn_paper = Button(
    master=frm_player,
    text="Бумага",
    font=("Comic Sans MS", 40, "bold"),
    bg="#575d7a",
    fg="white",
    width=7,
    height=1)

btn_scis = Button(
    master=frm_player,
    text="Ножница",
    font=("Comic Sans MS", 40, "bold"),
    bg="#575d7a",
    fg="white",
    width=7,
    height=1)

# ----------Event----------


# ----------Show widget----------
frm_title_game.pack()
frm_robot.pack(side=LEFT)
frm_player.pack(side=RIGHT)

lbl_title_robot.place(x=115, y=0)
lbl_title_plaver.place(x=115, y=0)

btn_stoun.place(relx=0.5, y=130, anchor=CENTER)
btn_paper.place(relx=0.5, y=220, anchor=CENTER)
btn_scis.place(relx=0.5, y=310, anchor=CENTER)



window.mainloop()