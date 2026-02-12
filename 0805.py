from tkinter import *

window = Tk()

window.title("My first GUI")
window.config(background="gray")
window.iconbitmap("g.jpg")

window.geometry("500x500")
window.resizable(1, 0)

txt = "Напиши да чтобы изменить цвет фона"
labl = Label(window,
             text=txt,
             foreground="black",
             bg="gray",
             width=40,
             height=2,
             )
labl.pack()

def f():
    global fon
    if fon == "да":
        window.config(background="red")

var = None
pole = Entry(window,
             fg="black",
             bg="white",
             width=40
             )
pole.pack()
fon = pole.get()

btn = Button(window,
             text="Отправить",
             command=f
             )
btn.pack()





window.mainloop()
print(fon)