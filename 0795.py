from tkinter import *

root = Tk()

root.title("Test")
root.iconbitmap("")
root.config(background="gray")

root.geometry("500x500")
root.resizable(0, 0)

text = input()

lb1 = Label(root,
            text=text,
            font=("Sans Serif", 50, "bold"),
            fg="yellow",
            bg="green",
            width=7,
            height=2
            )
lb1.pack()

#img = PhotoImage(file="photo.png")
#lb2 = Label(root, image=img)
#lb2.pack()


root.mainloop()

# Label -> text, font, fg, bg, width, height, image
# PhotoImage -> file