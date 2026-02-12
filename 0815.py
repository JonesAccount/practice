from tkinter import *

window = Tk()

# ----------Page----------
window.title("Coding Game")
window.config(bg="black")
window.geometry("800x600")
window.resizable(0, 0)

entry = Entry(window, width=40, fg="black")
entry.insert(0, "What is your name?")
entry.pack()

entry = Entry(window, width=40, fg="black")
entry.insert(END, "What is your name?")
entry.pack()

entry = Entry(window, width=40, fg="black", bg="white")
entry.insert(0, "What is your name?")
entry.pack()

entry = Entry(window, width=40)
entry.insert(0, "What is your name?")
entry.pack()

entry = Entry(window, width=40, fg="black")
entry.insert(END, "What is your name?")
entry.pack()

window.mainloop()