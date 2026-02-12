from tkinter import *
window = Tk()

window.title("GUI")
window.config(background="gray")

window.geometry("800x500")
window.resizable(0, 0)

lab = Label(window,
            text="Welcome",
            font=("Arial", 5, "bold")
            )
lab.pack()

entry = Entry(window)
entry.insert(0, "круто!")
entry.pack()

def edit():
    if entry.get() != "Python круто!":
        entry.insert(0, "Python ")
    entry.pack()
    
def edits():
    lab.insert(0, "TK")
    lab.pack()

btn = Button(window,
            text="Жми!",
            command=edit
            )
btn.pack()

btn1 = Button(window,
            text="Жми! (2)",
            command=edits
            )
btn1.pack()

window.mainloop()