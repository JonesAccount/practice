from random import *

ore = {"coals": 0, "iron": 0, "gold": 0, "diamond": 0}
progress = {"experience": 0, "level": 1}

def mine_location():
        print("\n————————————————————————————————")
        print("|MINE LOCATION|", end="         ")
        print(nickname)
        while True:
            dig = input(">> ")
            if dig == "dig coal" or dig == "d1":
                found_ore = randint(1, 6)
                found_experience = randint(5, 10)
                ore["coals"] += found_ore
                progress["experience"] += found_experience
                print("+", found_ore, "coal")
                print("+", found_experience, "experience\n")
            elif dig == "dig iron" or dig == "d2":
                if progress["level"] >= 2:
                    found_ore = randint(1, 4)
                    found_experience = randint(30, 50)
                    ore["iron"] += found_ore
                    progress["experience"] += found_experience
                    print("+", found_ore, "iron")
                    print("+", found_experience, "experience\n")
                else:
                    print("Iron will open level 2 :-/\n")
            elif dig == "dig gold" or dig == "d3":
                if progress["level"] >= 3:
                    found_ore = randint(1, 2)
                    found_experience = randint(90, 150)
                    ore["gold"] += found_ore
                    progress["experience"] += found_experience
                    print("+", found_ore, "gold")
                    print("+", found_experience, "experience\n")
                else:
                    print("Gold will open level 3 :-/\n")
            elif dig == "dig diamond" or dig == "d4":
                if progress["level"] >= 4:
                    found_ore = randint(1, 2)
                    found_experience = randint(200, 300)
                    ore["diamond"] += found_ore
                    progress["experience"] += found_experience
                    print("+", found_ore, "diamond")
                    print("+", found_experience, "experience\n")
                else:
                    print("Diamond will open level 4\ :-/n")
            elif dig == "stop":
                print("\n————————————————————————————————")
                game.menu()
            else:
                print("Wrong command :-/\n")

class Start:
    def __init__(self, x):
        self.x = 0
    def menu(self):
        house()
        
def house():
    print("|MENU|", end="                  ")
    print(nickname)
    print("Level:", progress["level"])
    print("Experience:", progress["experience"])
    print("Coal:", ore["coals"])
    print("Iron:", ore["iron"])
    print("Gold:", ore["gold"])
    print("Diamond", ore["diamond"])
    print("\n|COMMANDS|")
    print("1. Mine")
    print("2. Market")
    print("3. Help")
    print("4. Statistics")
    while True:
        action = input("\nAction: ")
        if action == "mine":
            mine_location()
        else:
            print("Wrong command :-/")
        
print("Welcome to my game!\n")
nickname = input("Your name? ")
print("\nI wish good games :)\n")
print("----------|START GAME|----------")

while True:
    game = Start(0)
    game.menu()
