from tkinter import *

window = Tk()

# ----------Page----------
window.title("Coding Game")
window.config(bg="black")
window.geometry("800x600")
window.resizable(0, 0)

# ----------Frame----------
frm = Frame(master=window, relief=RIDGE, borderwidth=5)
frm.pack()


# ----------Button----------
lbl_space = Label(
    width=30,
    height=1,
    bg="black",
    borderwidth=0,
)

btn_play = Button(
    text="Play",
    width=30,
    height=3,
    borderwidth=5,
)

# ----------Show widgets----------
lbl_space.pack()
btn_play.pack()


window.mainloop()