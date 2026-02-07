from random import randint as r

number: int = r(100, 999)
number: str = str(number)
    
print(f"Цифра: {number}\n")
print(f"Разряд единиц: {number[-1:]}", end="")
print(f" | {number[-1:]} * 1")

print(f"Разряд десятков: {number[1:2]}", end="")
print(f" | {number[1:2]} * 10")
    
print(f"Разряд сотен: {number[:-2]}", end="")
print(f" | {number[:-2]} * 100\n")

print(f"{number[:-2]}00 + {number[1:2]}0 + {number[-1:]} = {number}")