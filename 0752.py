def calcu(width: float, height: float) -> float:
    return width * height

print(calcu(4, 5))

def greet(name: str, age: int) -> str:
    return f"{name} is {age} years old"

print(greet("Eva", 18))

def numbers(number: int | float = 5) -> int | float:
    res = number / 4
    return res

print(numbers())