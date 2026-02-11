import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"
    page.theme_mode = "dark"

    def cal_plus(e):
        num1 = float(number1.value)
        num2 = float(number2.value)
        res = num1 + num2
        result.value = f"результат: {res}"
        page.update()

    def cal_minus(e):
        num1 = float(number1.value)
        num2 = float(number2.value)
        res = num1 - num2
        result.value = f"результат: {res}"

    def cal_multiply(e):
        num1 = float(number1.value)
        num2 = float(number2.value)
        res = num1 * num2
        result.value = f"результат: {res}"

    def cal_division(e):
        num1 = float(number1.value)
        num2 = float(number2.value)
        res = num1 / num2
        result.value = f"результат: {res}"


    button_plus = ft.ElevatedButton("сложить", on_click=cal_plus)
    button_minus = ft.ElevatedButton("вычитать", on_click=cal_minus)
    button_multip = ft.ElevatedButton("умножить", on_click=cal_multiply)
    button_division = ft.ElevatedButton("делить", on_click=cal_division)

    title = ft.Text("калькулятор", size=30, weight="bold", color="brown")
    probel = ft.Text()

    number1 = ft.TextField(label="первое число", width=250)
    number2 = ft.TextField(label="второе число", width=250)
    result = ft.Text("результат: ", size=20)

    page.add(
        title,
        probel,
        ft.Row(controls=[ft.Text("▶️"), number1]),
        ft.Row(controls=[ft.Text("▶️"), number2]),
        ft.Row(controls=[button_plus, button_minus, button_multip, button_division]),
        probel,
        result
    )
if name == "main":
    ft.run(main)