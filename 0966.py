from time import sleep as son
from random import randint
from cowsay import cow
import os

wallet: int = 10000
    
year: int = None
summa: int = None
age: int = 20
summa_for_wallet: int = 0
    
line_break: str = "\n"
show = print


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def error_input():
    son(2)
    clear()
    

def main():
    while (1 == 1):
        show("Класть деньги в депозит?")
        show("[1] - да")
        show("[2] - нет")
        try:
            do = int(input(f"{line_break}Действие: "))
            if do == 1:
                clear()
                deposit_sum()
            elif do == 2:
                cow("Пока")
                son(2)
                break  
            else:
                cow("Что?...")
                error_input()
        except ValueError:
            cow("Что?...")
            error_input()
            
    
def result():
    global wallet
    counter = 3
    loading = list("-------")
    line = "|"
    while counter > 0:
        for i in range(8):
            loading.insert(i, "o")
            show(line, "".join(loading), line, sep="")
            loading.pop(loading.index("o"))
            son(0.1)
            clear()
        counter -= 1
        
    clear()
    show(f"Прошло {year} лет / год\n")
    show(f"Изначальная сумма: {round((wallet + summa_for_wallet), 0)}$")
    show(f"Вложение: {summa_for_wallet}$")
    show(f"После вклада: {round((wallet + summa), 0)}$")
    show(f"Вознаграждение: {round(summa - summa_for_wallet, 0)}$")
    wallet += summa
    end = input(f"{line_break}Нажми enter")
    clear()
    main()
    
    
def deposit_time():
    global year, summa, age
    while True:
        show("На какой срок?")
        try:
            year = int(input("\nЛет: "))
            percent = randint(5, 17)
            percent_month = percent / 12 / 100
            if 0 < year < 82:
                if age + year < 102:
                    all_year = year * 12
                    for i in range(all_year):
                        summa *= (1 + percent_month)
                    age += year
                    result()
                else:
                    show(f"Тебе {age}, можно только до {101 - (age)} лет")
                    error_input()
            elif year < 1:
                cow("Слишком мало")
                error_input()
            else:
                cow("Не доживешь")
                error_input()
        except:
            cow("Что?...")
            error_input()
            
    

def deposit_sum():
    global summa, wallet, summa_for_wallet
    while bool("Husking") == True:
        show(f"Твой счёт: {round(wallet, 0)}$")
        show(f"Твой возраст: {age}")
        try:
            summa = int(input(f"{line_break}Сколько класть: "))
            summa_for_wallet = summa
            if wallet >= summa:
                wallet -= summa
                clear()
                deposit_time()
            else:
                cow("Не жирно тебе?")
                error_input()
        except ValueError:
            cow("Что?...")
            error_input()
            
main()
clear()