def factorial(number: int = 5) -> int:
    """
    Описание: Вычисляет факториал числа number.
    number: int - неотрицательное целое число.
    Возвращает : int - факториал числа number.
    """
    result: int = 1
    for n in range(1, number + 1):
        result *= n
    return result


def factorial_test(func) -> int:
    """
    Описание: тест для функции factorial.
    Результат: заданное число n в тесте должно вернуть факториал. 
    """
    n = 5 # факториал 5 – 120
    result = func(n)
    print("Успешно!" if result == 120 else "Провал")


factorial_test(factorial)