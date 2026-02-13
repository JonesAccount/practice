from tkinter import *

window = Tk()

# ----------Page----------
window.title("Program")
window.config(bg="black")
window.geometry("800x600")
window.resizable(0, 0)


# ----------Variable----------


# ----------Function----------
def enter(event):
    btn2.config(text="0")

def leave(event, x: str = "2"):
    btn2.config(text=x)

# ----------Frame----------


# ----------Label----------


# ----------Entry----------


# ----------Text----------


# ----------Button----------
btn1 = Button(master=window,text="1", font=("palation", 50, "bold"))
btn2 = Button(master=window,text="2", font=("calibri", 50, "bold"))


# ----------Show widget----------
btn1.pack(side=LEFT)
btn2.pack(side=LEFT, padx=50)

btn2.bind("<Enter>", enter)
btn2.bind("<Leave>", leave)


window.mainloop()