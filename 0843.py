from tkinter import *

window = Tk()

# ----------Page----------
window.title("Факториал")
window.config(bg="black")
window.geometry("800x600")
window.resizable(0, 0)


# ----------Variable----------


# ----------Function----------
def fac(event):
    if ent_number.get().isdigit():
        res = 1
        n = int(ent_number.get())
        for x in range(1, n + 1):
            res *= x
        lbl_result.config(text=str(res))


# ----------Frame----------
frm_head = Frame(
    master=window,
    bg="black",
    width=800,
    height=120)

frm_body = Frame(
    master=window,
    bg="black",
    width=800,
    height=480)


# ----------Label----------
lbl_title = Label(
    master=frm_head,
    text="Факториал числа",
    font="Tahoma 40 bold",
    fg="white",
    bg="black")

lbl_number = Label(
    master=frm_body,
    text="Число:",
    font="Tahoma 30 bold",
    fg="white",
    bg="black")

lbl_title_result = Label(
    master=frm_body,
    text="Результат:",
    font="Tahoma 30 bold",
    fg="white",
    bg="black")

lbl_result = Label(
    master=frm_body,
    text="0",
    font="Tahoma 30 bold",
    fg="white",
    bg="black")


# ----------Entry----------
ent_number = Entry(
    master=frm_body)


# ----------Text----------


# ----------Button----------


# ----------Event----------
ent_number.bind("<KeyRelease>", fac)


# ----------Show widget----------
frm_head.pack(side=TOP); frm_body.pack(side=TOP, fill=BOTH, expand=True)

lbl_title.place(relx=0.5, rely=0.5, anchor=CENTER)
lbl_number.grid(row=0, column=0, padx=200 - 20, pady=100); ent_number.grid(row=0, column=1)
lbl_title_result.grid(row=1, column=0, pady=100); lbl_result.grid(row=1, column=1)


window.mainloop()