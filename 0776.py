import flet as ft

def main(page: ft.Page):
    page.title = "My program"
    page.add(ft.Text(value="Добро пожаловать!"))
    text = ft.Text(value="Пока не знаю че писать")

    page.add(
        ft.Row(controls=[text]),
        ft.Row(
            controls=[
                ft.Button("Button 1"),
                ft.Button("Button 2"),
                ft.Button("Button 3"),
                ft.Button("Button 4"),
                ft.Button("Button 5")
            ]
        ),
        ft.Row(
            controls=[
                ft.Button("Button 1"),
                ft.Button("Button 2"),
                ft.Button("Button 3"),
                ft.Button("Button 4"),
                ft.Button("Button 5")
            ]
        ),
        ft.Row(
            controls=[
                ft.Button("Button 1"),
                ft.Button("Button 2"),
                ft.Button("Button 3"),
                ft.Button("Button 4"),
                ft.Button("Button 5")
            ]
        )
    )

if __name__ == "__main__":
    ft.run(main)