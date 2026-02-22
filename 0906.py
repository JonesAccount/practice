from tkinter.constants import CENTER

import customtkinter as ctk

window = ctk.CTk()
window.title("Кино-дневник")

# настройки размеры и координаты окна
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = int(screen_width * 0.85)
window_height = int(screen_height * 0.85)
X = (screen_width - window_width) // 2
Y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{X}+{Y}")
window.resizable(False, False)


frm_navigation = ctk.CTkFrame(
    master=window,
    fg_color="orange",
    width=150
); frm_navigation.pack(side="left", fill="y")


frm_details = ctk.CTkFrame(
    master=window,
    fg_color="green",
    width=250
); frm_details.pack(side="right", fill="y")


frm_content = ctk.CTkFrame(
    master=window,
    fg_color="blue"
); frm_content.pack(side="left", fill="both", expand=True)


frm_header = ctk.CTkFrame(
    master=frm_content,
    fg_color="red",
    height=100
); frm_header.pack(side="top", fill="x")

def resize_entry_search(event):
    header_width = event.width
    ent_search.configure(width=header_width - 270); ent_search.place(x=0, y=70)
    btn_search.place(x=865, y=70)

ent_search = ctk.CTkEntry(
    master=frm_header
)

frm_header.bind("<Configure>", resize_entry_search)


btn_search = ctk.CTkButton(
    master=frm_header,
    text="⟳",
    width=35,
    height=28
)



window.mainloop()

# winfo_screenwidth()
# winfo_screenheight()
# bg_color
# CTkFrame
# CTkEntry
# CTkButton
# fg_color
# configure