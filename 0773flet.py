from time import sleep
import flet as ft
from flet import control


def main(page: ft.Page):
    page.title = "Мое приложение"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    input = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        input.value = str(int(input.value) - 1)
    def plus_click(e):
        input.value = str(int(input.value) + 1)

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                input,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
        )
    )


ft.run(main)

# text1 = ft.Text(value="Мое первое приложение!", color="blue")
# text2 = ft.Text(value="Это второй текст 😍", color="yellow")
# text3 = ft.Text(value="Мне пока нравиться этот фреймворк ✅", color="red")
# page.controls.append(text1)
# page.controls.append(text2)
# page.controls.append(text3)
# page.update()
#
# for i in range(10):
#     text2.value = f" Шаг {i + 1}"
#     page.update()
#     sleep(1)
