from tkinter import *

window = Tk()

def close_program():
    window.destroy()

counter_notes = 1
def save_note():
    with open(f"document {counter_notes}", "w") as file:
        file.write(txt.get(1.0, END))

# ----------Page----------
window.title("Текстовый редактор")
window.geometry("800x600")
window.resizable(True, True)


# ----------Главное меню----------
menu = Menu(master=window)
window.config(bg="black", menu=menu)


# ----------Раздел Файл----------
menu_file = Menu(master=menu, tearoff=False)
menu.add_cascade(label="Файл", menu=menu_file)

menu_file.add_command(label="Создать")
menu_file.add_command(label="Открыть...")
menu_file.add_command(label="Сохранить")
menu_file.add_command(label="Сохранить как...")
menu_file.add_separator()
menu_file.add_command(label="Параметры страницы...")
menu_file.add_command(label="Печать...")
menu_file.add_separator()
menu_file.add_command(label="Выход", command=close_program)


# ----------Раздел Правка----------
menu_edit = Menu(master=menu, tearoff=False)
menu.add_cascade(label="Правка", menu=menu_edit)

menu_edit.add_command(label="Отменить")
menu_edit.add_separator()
menu_edit.add_command(label="Вырезать")
menu_edit.add_command(label="Копировать")
menu_edit.add_command(label="Вставить")
menu_edit.add_command(label="Удалить")
menu_edit.add_separator()
menu_edit.add_command(label="Найти...")
menu_edit.add_command(label="Найти далее")
menu_edit.add_command(label="Заменить...")
menu_edit.add_command(label="Перейти")
menu_edit.add_separator()
menu_edit.add_command(label="Выделить все")
menu_edit.add_command(label="Время и дата")


# ----------Раздел Формат----------
menu_format = Menu(master=menu, tearoff=False)
menu.add_cascade(label="Формат", menu=menu_format)

menu_format.add_command(label="Перенос по словам")
menu_format.add_command(label="Шрифт...")


# ----------Раздел Вид----------
menu_show = Menu(master=menu, tearoff=False)
menu.add_cascade(label="Вид", menu=menu_show)

menu_show.add_command(label="Строка состояния")


# ----------Раздел Справка----------
menu_help = Menu(master=menu, tearoff=False)
menu.add_cascade(label="Справка", menu=menu_help)

menu_help.add_command(label="Просмотреть справку")
menu_help.add_command(label="О программе")


# ----------Variable----------


# ----------Function----------


# ----------Frame----------


# ----------Label----------


# ----------Entry----------


# ----------Text----------
txt = Text(
    master=window,
    font=("Arial", 15),
    bg="black",
    fg="white")
scroll = Scrollbar(master=window)
scroll.config(command=txt.yview)
txt.config(yscrollcommand=scroll.set)

# ----------Button----------


# ----------Event----------



# ----------Show widget----------
txt.pack(fill=BOTH, side=LEFT, expand=True)
scroll.pack(fill=Y, side=RIGHT)


window.mainloop()