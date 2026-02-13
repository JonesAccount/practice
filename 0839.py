from tkinter import *

window = Tk()

# ----------Page----------
window.title("Clicker")
window.config(bg="black")
window.geometry("500x700")
window.resizable(0, 0)


# ----------Variable----------
clicks = 0
click_lvl = 1
autoclick_lvl = 0
prise_autoclick = 50


# ----------Function----------
def click(event):
    global clicks
    clicks += click_lvl
    lbl_text_click.config(text=clicks)

def update_autoclick():
    global click_lvl, autoclick_lvl, prise_autoclick, clicks
    if clicks >= prise_autoclick:
        autoclick_lvl += 1
        clicks -= prise_autoclick
        prise_autoclick *= 2
        lbl_update_auto["text"] = f"upgrade: {prise_autoclick}"
    if autoclick_lvl > 0:
        clicks += autoclick_lvl
        lbl_text_click.config(text=clicks)
        window.after(1000, update_autoclick)

def start_autoclick(event):
    update_autoclick()


# ----------Frame----------


# ----------Label----------
lbl_text_click = Label(master=window, text="0", font=("Segoe UI", 80, "bold"), bg="black", fg="white")
lbl_update_auto = Label(master=window, text=f"upgrade: {prise_autoclick}", font=("Segoe UI", 20, "bold"), bg="black", fg="white")


# ----------Entry----------


# ----------Text----------


# ----------Button----------
btn_click = Button(master=window, text="click", font="Impact 50 bold", bg="black", fg="black")
btn_autoclick = Button(master=window, text="autoclick", font="Impact 50 bold", bg="black", fg="black")


# ----------Event----------
btn_click.bind("<Button-1>", click)
btn_autoclick.bind("<Button-1>", start_autoclick)


# ----------Show widget----------
lbl_text_click.place(relx=0.5, y=260, anchor=CENTER)
lbl_update_auto.place(relx=0.5, y=600, anchor=CENTER)

btn_click.place(relx=0.5, y=450, anchor=CENTER)
btn_autoclick.place(relx=0.5, y=550, anchor=CENTER)


window.mainloop()