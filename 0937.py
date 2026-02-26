from time import sleep
from sys import exit
import os

# Создание игровых клеток
keys = [i for i in range(1, 10)]

# Переменные
counter_standoff = False
space: str = " " * 11
line_break: str = "\n"
players: str = "player1"


class Logic:
    def play(self):
        global players
        utils = Utils(); utils.text()
        
        def forever(self) -> True:
            while True == 1:
                yield

        while not (not forever(self)):
            try:
                counter_standoff = True if all(isinstance(x, str) for x in keys) else None
        
                if counter_standoff == True:
                    print(line_break + (space + space[:len(space) // 2]) + "ничья!")
                    print(line_break * 3)
                    exit()

                step = int(input((space + space[:3]) + f"игрок: Х\n{space + space[:3]}клетка: " if players == "player1" else f"{space + space[:3]}игрок: O\n{space + space[:3]}клетка: "))
                if 0 < step < 10:
                    if isinstance(keys[step - 1], int):
                        break
                    else:
                        print(line_break + (space + space[0]) + "клетка занята"); sleep(1)
                        os.system("cls" if os.name == "nt" else "clear")
                        text()
                else:
                    utils = Utils(); utils.error_input()
            except ValueError:
                utils.error_input()
                
        keys[step - 1] = "X" if players == "player1" else "O"
        
        os.system("cls" if os.name == "nt" else "clear")
        
        # Проверка на комбинаций
        check = Check()
        check.check_horizontal(); check.check_vertical(); check.check_diagonal()
        
        players = "player2" if players == "player1" else "player1"
            
        self.play()


class Check:
    def check_horizontal(self):
        check = []; counter = 0; start = 0
        for i in range(start, len(keys)):
            check.append(keys[i]); counter += 1
            if counter == 3:
                counter = 0; check = set(check)
                if len(check) == 1:
                    utils = Utils(); utils.text()
                    print(line_break + space + "Игрок", end="")
                    print(" 1 победил!" if players  == "player1" else " 2 победил!")
                    print(line_break * 3)
                    exit()
                else:
                    check = list()
                start += 3
    
    def check_vertical(self):
        # Проверка 1 колонны
        checks = set()
        checks.add(keys[0]); checks.add(keys[3]); checks.add(keys[6])
        if len(checks) == 1:
            utils = Utils(); utils.text()
            print(line_break + space + "Игрок", end=""); print(" 1 победил!" if players  == "player1" else " 2 победил!")
            print(line_break * 3)
            exit()
            
        # Проверка 2 колонны
        checks = set()
        checks.add(keys[1]); checks.add(keys[4]); checks.add(keys[7])
        if len(checks) == 1:
            utils = Utils(); utils.text()
            print(line_break + space + "Игрок", end=""); print(" 1 победил!" if players  == "player1" else " 2 победил!")
            print(line_break * 3)
            exit()
            
        # Проверка 3 колонны
        checks = set()
        checks.add(keys[2]); checks.add(keys[5]); checks.add(keys[8])
        if len(checks) == 1:
            utils = Utils(); utils.text()
            print(line_break + space + "Игрок", end=""); print(" 1 победил!" if players  == "player1" else " 2 победил!")
            print(line_break * 3)
            exit()
              
    def check_diagonal(self):
        # Проверка 1-5-9
        checks = set()
        checks.add(keys[0]); checks.add(keys[4]); checks.add(keys[8])
        if len(checks) == 1:
            utils = Utils(); utils.text()
            print(line_break + space + "Игрок", end=""); print(" 1 победил!" if players  == "player1" else " 2 победил!")
            print(line_break * 3)
            exit()
            
        # Проверка 3-5-7
        checks = set()
        checks.add(keys[2]); checks.add(keys[4]); checks.add(keys[6])
        if len(checks) == 1:
            utils = Utils(); utils.text()
            print(line_break + space + "Игрок", end=""); print(" 1 победил!" if players  == "player1" else " 2 победил!")
            print(line_break * 3)
            exit()


class Utils:
    # Отображение игрового поля
    def text(self):
        counter = 0
        print(line_break * 2 + space + f"крестики-нолики{line_break * 2}")
        for i in range(0, len(keys), 3):
            print((space + space[:3]) + " | ".join(str(keys[j]) for j in range(i, i + 3)))
            counter += 1
            if counter == 3:
                print(); counter = 0
        print()
        
    def error_input(self) -> str:
        print(line_break + space[:-2] + "ввод не корректный"); sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        utils = Utils(); utils.text()

logic = Logic()
logic.play()
