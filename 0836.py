from random import choice
from tkinter import *

window = Tk()

# ----------Page----------
window.title("КНБ")
window.config(bg="black")
window.geometry("800x600")
window.resizable(0, 0)


# ----------Variable----------
knb_player = None; knb_robot = None
counter_wins_player = 0; counter_wins_robot = 0


# ----------Function----------
def stoun(event):
    global knb_player
    knb_player = "к"
    robot_choice()

def paper(event):
    global knb_player
    knb_player = "б"
    robot_choice()

def scis(event):
    global knb_player
    knb_player = "н"
    robot_choice()

def robot_choice():
    global knb_robot
    lst = ["к", "б", "н"]
    knb_robot = choice(lst)
    logic()

def logic():
    global counter_wins_player, counter_wins_robot
    if knb_player == knb_robot:
        lbl_res.config(text="Ничья", fg="orange")
    elif knb_player == "к" and knb_robot == "н":
        lbl_res.config(text="ПОБЕДА!", fg="green")
        counter_wins_player += 1
        lbl_wins_plaver.config(text=f"Выигрыши: {counter_wins_player}")
    elif knb_player == "к" and knb_robot == "б":
        lbl_res.config(text="ПОРАЖЕНИЕ!", fg="red")
        counter_wins_robot += 1
        lbl_wins_robot.config(text=f"Выигрыши: {counter_wins_robot}")
    elif knb_player == "н" and knb_robot == "к":
        lbl_res.config(text="ПОРАЖЕНИЕ!", fg="red")
        counter_wins_robot += 1
        lbl_wins_robot.config(text=f"Выигрыши: {counter_wins_robot}")
    elif knb_player == "н" and knb_robot == "б":
        lbl_res.config(text="ПОБЕДА!", fg="green")
        counter_wins_player += 1
        lbl_wins_plaver.config(text=f"Выигрыши: {counter_wins_player}")
    elif knb_player == "б" and knb_robot == "к":
        lbl_res.config(text="ПОБЕДА!", fg="green")
        counter_wins_player += 1
        lbl_wins_plaver.config(text=f"Выигрыши: {counter_wins_player}")
    elif knb_player == "б" and knb_robot == "н":
        lbl_res.config(text="ПОРАЖЕНИЕ!", fg="red")
        counter_wins_robot += 1
        lbl_wins_robot.config(text=f"Выигрыши: {counter_wins_robot}")


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
    text="🤖РОБОТ",
    font=("Comic Sans MS", 40, "bold"),
    bg="#575d7a",
    fg="white")

lbl_title_plaver = Label(
    master=frm_player,
    text="👤ИГРОК",
    font=("Comic Sans MS", 40, "bold"),
    bg="#575d7a",
    fg="white")

lbl_wins_robot = Label(
    master=frm_robot,
    text=f"Выигрыши: {counter_wins_robot}",
    font=("Comic Sans MS", 30, "bold"),
    bg="#575d7a",
    fg="white")

lbl_wins_plaver = Label(
    master=frm_player,
    text=f"Выигрыши: {counter_wins_player}",
    font=("Comic Sans MS", 30, "bold"),
    bg="#575d7a",
    fg="white")

lbl_res = Label(
    master=frm_title_game,
    text="КАМЕНЬ БУМАГА НОЖНИЦА",
    font=("Comic Sans MS", 35, "bold"),
    bg="#575d7a",
    fg="gray")


# ----------Button----------
btn_stoun_robot = Button(
    master=frm_robot,
    text="Камень",
    font=("Comic Sans MS", 40, "bold"),
    bg="#575d7a",
    fg="black",
    width=7,
    height=1)

btn_paper_robot = Button(
    master=frm_robot,
    text="Бумага",
    font=("Comic Sans MS", 40, "bold"),
    bg="#575d7a",
    fg="black",
    width=7,
    height=1)

btn_scis_robot = Button(
    master=frm_robot,
    text="Ножница",
    font=("Comic Sans MS", 40, "bold"),
    bg="black",
    fg="black",
    width=7,
    height=1)

btn_stoun_player = Button(
    master=frm_player,
    text="Камень",
    font=("Comic Sans MS", 40, "bold"),
    bg="#575d7a",
    fg="black",
    width=7,
    height=1)

btn_paper_player = Button(
    master=frm_player,
    text="Бумага",
    font=("Comic Sans MS", 40, "bold"),
    bg="#575d7a",
    fg="black",
    width=7,
    height=1)

btn_scis_player = Button(
    master=frm_player,
    text="Ножница",
    font=("Comic Sans MS", 40, "bold"),
    bg="black",
    fg="black",
    width=7,
    height=1)

# ----------Event----------
btn_stoun_player.bind("<Button-1>", stoun)
btn_paper_player.bind("<Button-1>", paper)
btn_scis_player.bind("<Button-1>", scis)


# ----------Show widget----------
frm_title_game.pack()
frm_robot.pack(side=LEFT)
frm_player.pack(side=RIGHT)

lbl_title_robot.place(x=100, y=0)
lbl_title_plaver.place(x=100, y=0)
lbl_wins_plaver.place(relx=0.5, y=440, anchor=CENTER)
lbl_wins_robot.place(relx=0.5, y=440, anchor=CENTER)
lbl_res.place(relx=0.5, rely=0.5, anchor=CENTER)

btn_stoun_player.place(relx=0.5, y=130, anchor=CENTER)
btn_paper_player.place(relx=0.5, y=220, anchor=CENTER)
btn_scis_player.place(relx=0.5, y=310, anchor=CENTER)
btn_stoun_robot.place(relx=0.5, y=130, anchor=CENTER)
btn_paper_robot.place(relx=0.5, y=220, anchor=CENTER)
btn_scis_robot.place(relx=0.5, y=310, anchor=CENTER)


window.mainloop()