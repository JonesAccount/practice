from tkinter import *

window = Tk()

# ----------Page----------
window.title("Program")
window.config(bg="black")
window.geometry("800x600")
window.resizable(0, 0)


# ----------Variable----------


# ----------Function----------


# ----------Frame----------


# ----------Label----------


# ----------Entry----------


# ----------Text----------


# ----------Button----------
btn1 = Button(
    master=window,
    text="1",
    font=("Arial", 100, "bold"),
    fg="black",
    bg="brown")

btn2 = Button(
    master=window,
    text="2",
    font=("Arial", 100, "bold"),
    fg="black",
    bg="brown")

btn3 = Button(
    master=window,
    text="3",
    font=("Arial", 100, "bold"),
    fg="black",
    bg="brown")

btn4 = Button(
    master=window,
    text="4",
    font=("Arial", 100, "bold"),
    fg="black",
    bg="brown")


# ----------Show widget----------
btn1.grid(row=0, column=0, pady=50); btn2.grid(row=0, column=1, padx=50, pady=50)
btn3.grid(row=1, column=0, padx=50); btn4.grid(row=1, column=1)




window.mainloop()