from tkinter import *

window = Tk()

# ----------Page----------
window.title("Coding Game")
window.config(bg="white")
window.geometry("800x600")
window.resizable(0, 0)

lbl_1 = Label(window, text=".", font=("Arial", 300, "bold"), bg="white", fg="red")
lbl_2 = Label(window, text=".", font=("Arial", 300, "bold"), bg="white", fg="yellow")

lbl_1.pack(); lbl_2.pack()

window.mainloop()