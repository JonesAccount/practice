from tkinter import *

window = Tk()

# ----------Page----------
window.title("Оставить отзыв")
window.config(bg="gray")
window.geometry("800x600")
window.resizable(0, 0)


# ----------Variable----------


# ----------Function----------


# ----------Frame----------


# ----------Label----------
lbl_title = Label(
    master=window,
    text="Заголовок",
    font=("Arial", 30),
    bg="gray",
    fg="black")

lbl_author = Label(
    master=window,
    text="Автор",
    font=("Arial", 30),
    bg="gray",
    fg="black")

lbl_think = Label(
    master=window,
    text="Отзыв",
    font=("Arial", 30),
    bg="gray",
    fg="black")


# ----------Entry----------
entry_title = Entry(
    master=window,
    bg="gray",
    fg="black",
    insertbackground="black")

entry_author = Entry(
    master=window,
    bg="gray",
    fg="black",
    insertbackground="black")

# ----------Text----------
txt = Text(
    master=window,
    bg="gray",
    fg="black",
    insertbackground="black")


# ----------Button----------


# ----------Show widget----------
lbl_title.place(x=10, y=10)
lbl_author.place(x=10, y=100)
lbl_think.place(x=10, y=190)

entry_title.place(x=200, y=17)
entry_author.place(x=200, y=108)

txt.place(x=200, y=200)



window.mainloop()