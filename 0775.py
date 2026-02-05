import flet as ft


def main(page: ft.Page):
    page.title = "App Flet"

    page.add(ft.Text(value="Приветик, Flet!", color="grey"))
    page.add(ft.Text(value=""))
    text = ft.Text(value="Внизу кнопочки:")

    page.add(
        text,
        ft.Button("Кнопка 1"),
        ft.Button("Кнопка 2"),
        ft.Button("Кнопка 3")
    )


if __name__ == "__main__":
    ft.run(main)
