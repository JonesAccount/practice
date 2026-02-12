from tkinter import *

root = Tk()

root.title("My first GUI")
root.config(background="gray")
root.iconbitmap("g.jpg")

root.geometry("500x500")
root.resizable(1, 0)

x, y = 500, 500
def click():
    #root.geometry(f"{x - 10}x{y - 10}")
    root.geometry("800x600")

btn1 = Button(root,
              text="Click",
              font=("Arial", 20, "bold"),
              bg="red",
              fg="black",
              activebackground="red",
              activeforeground="black",
              width=10,
              height=1,
              command=click
              )
btn1.pack()

lbl1 = Label(root,
              text="Click",
              font=("Arial", 20, "bold"),
              bg="red",
              fg="black",
              activebackground="red",
              activeforeground="black",
              width=10,
              height=1,
              )
lbl1.pack()


root.mainloop()