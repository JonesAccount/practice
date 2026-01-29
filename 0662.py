# Переменые
play_game = False
line = "-" * 30
dot = "•   •   •   •   •   •   •   •"
space = " "
action_home = None
action_tree = None
action_shop = None
tree = 0
coin = 0
topor_lvl = 1 # уровень
topor_lvl2_coin = 50
topor_lvl3_coin = 250
topor_lvl4_coin = 888

print("• ИГРА ДРОВОСЕК •", end="\n\n")

print("Добро пожаловать в мою мини-игру, это первый пет-проект, строго не суди:)")

while True:
    name = input("\nСначала узнаем твое имя: напиши от 4 до 10 букв: ")
    if len(name) >= 4 and len(name) <= 10:
        print("\nПриятной игры, " + name + "!", end="\n\n")
        print(line)
        break
    else:
        continue
        
while True:
    # это локация дом
    if play_game == True:
        print("\n", line, sep="")
        for i in range(10):
            print(dot)
        print(line)
    if len(name) == 4:
        print("name: " + str(name) + space * 14 + "id8436")
    elif len(name) == 5:
        print("name: " + str(name) + space * 13 + "id8436")
    elif len(name) == 6:
        print("name: " + str(name) + space * 12 + "id8436")
    elif len(name) == 7:
        print("name: " + str(name) + space * 11 + "id8436")
    elif len(name) == 8:
        print("name: " + str(name) + space * 10 + "id8436")
    elif len(name) == 9:
        print("name: " + str(name) + space * 9 + "id8436")
    elif len(name) == 10:
        print("name: " + str(name) + space * 8 + "id8436")
    print(line)
    play_game = True
    
    print("|КОМАНДЫ|   |ДОМ|")
    print("• Мастерская")
    print("• Рынок")
    print("• Лес", end="\n\n")
    
    print("|ИНВЕНТАРЬ|")
    print("• Топор ур.", topor_lvl)
    print("• Дерево:", tree)
    print("• Монеты:", coin)
    
    print(line)
    
    loop = True
    while loop:
        action_home = input("|Действие >>> ")
        
        # это локация лес
        if action_home == "Лес" or action_home == "лес":
            print("\n", line, sep="")
            for i in range(10):
                print(dot)
            print(line)
            if len(name) == 4:
                print("name: " + str(name) + space * 14 + "id8436")
            elif len(name) == 5:
                print("name: " + str(name) + space * 13 + "id8436")
            elif len(name) == 6:
                print("name: " + str(name) + space * 12 + "id8436")
            elif len(name) == 7:
                print("name: " + str(name) + space * 11 + "id8436")
            elif len(name) == 8:
                print("name: " + str(name) + space * 10 + "id8436")
            elif len(name) == 9:
                print("name: " + str(name) + space * 9 + "id8436")
            elif len(name) == 10:
                print("name: " + str(name) + space * 8 + "id8436")
            print(line)
        
            print("|КОМАНДЫ|   |ЛЕС|")
            print("• Рубить")
            print("• Домой")
        
            while loop:
                action_tree = input("\n|Действие >>> ")
                if action_tree == "Рубить" or action_tree == "рубить" or action_tree == "Рубит" or action_tree == "рубит":
                    while loop:
                        print("\n+ 1 дерево")
                        tree +=1
                        action_tree = input("\n|Действие >>> ")
                        if action_tree == "Рубить" or action_tree == "рубить" or action_tree == "Рубит" or action_tree == "рубит":
                            continue
                        elif action_tree == "домой" or action_tree == "Домой" or action_tree == "Дом" or action_tree == "дом":
                            loop = False
                        else:
                            break
                elif action_tree == "домой" or action_tree == "Домой" or action_tree == "Дом" or action_tree == "дом":
                    loop = False
                else:
                    continue

# это локация рынок
        elif action_home == "Рынок" or action_home == "рынок":
            print("\n", line, sep="")
            for i in range(10):
                print(dot)
            print(line)
            if len(name) == 4:
                print("name: " + str(name) + space * 14 + "id8436")
            elif len(name) == 5:
                print("name: " + str(name) + space * 13 + "id8436")
            elif len(name) == 6:
                print("name: " + str(name) + space * 12 + "id8436")
            elif len(name) == 7:
                print("name: " + str(name) + space * 11 + "id8436")
            elif len(name) == 8:
                print("name: " + str(name) + space * 10 + "id8436")
            elif len(name) == 9:
                print("name: " + str(name) + space * 9 + "id8436")
            elif len(name) == 10:
                print("name: " + str(name) + space * 8 + "id8436")
            print(line)
        
            print("|КОМАНДЫ|   |РЫНОК|")
            print("• Продать дерево")
            print("• Домой")
        
            while loop:
                action_shop = input("\n|Действие >>> ")
                if action_shop == "Продать дерево" or action_shop == "продать дерево" or action_shop == "продать дерев":
                    if tree > 0:
                        while True:
                           print("\n+ " + str(tree * 5) + " монета (продано " + str(tree) + " дерево)")
                           coin += tree * 5
                           tree = 0
                           break
                    else:
                        print("\nНет дерево на продажу :(")
                elif action_shop == "домой" or action_shop == "Домой" or action_shop == "Дом" or action_shop == "дом":
                    loop = False
                else:
                    continue 
            
        # это локация мастерская
        elif action_home == "Мастерская" or action_home == "мастерская" or action_home == "Мастер" or action_home == "мастер":
            print("\n", line, sep="")
            for i in range(10):
                print(dot)
            print(line)
            if len(name) == 4:
                print("name: " + str(name) + space * 14 + "id8436")
            elif len(name) == 5:
                print("name: " + str(name) + space * 13 + "id8436")
            elif len(name) == 6:
                print("name: " + str(name) + space * 12 + "id8436")
            elif len(name) == 7:
                print("name: " + str(name) + space * 11 + "id8436")
            elif len(name) == 8:
                print("name: " + str(name) + space * 10 + "id8436")
            elif len(name) == 9:
                print("name: " + str(name) + space * 9 + "id8436")
            elif len(name) == 10:
                print("name: " + str(name) + space * 8 + "id8436")
            print(line)
        
            print("|КОМАНДЫ|   |МАСТЕРСКАЯ|")
            print("• Улучшить топор lvl" + str(topor_lvl) + " > " + "lvl" + str(topor_lvl + 1))
            print("• Купить бензопилу")
            
            print("\n|ИНФОРМАЦИЯ|")
            print("• Топор ур.", topor_lvl)
            if topor_lvl == 1:
                print("• Следущее улучшение: 50 монет")
            elif topor_lvl == 2:
                print("• Следущее улучшение: 250 монет")
            elif topor_lvl == 3:
                print("• Следущее улучшение: 888 монет")
            print("• Монеты:", coin)
        
            while loop:
                action_master = input("\n|Действие >>> ")
                if action_master == "Улучшить топор" or action_master == "Улучшить" or action_master == "улучшить" or action_master == "улучшить топор" or action_master == "улучшит":
                    if topor_lvl == 1:
                        if coin >= 50:
                            topor_lvl += 1
                            coin -= 50
                            print("\nТопор улучшен 1lvl >>> 2lvl!")
                            print("- 50 монет")
                        else:
                            print("\nНедостаточно монет :(")
                    elif topor_lvl == 2:
                        if coin >= 250:
                            topor_lvl += 1
                            coin -= 250
                            print("\nТопор улучшен 2lvl >>> 3lvl!")
                            print("- 250 монет")
                        else:
                            print("\nНедостаточно монет :(")
                    elif topor_lvl == 3:
                        if coin >= 888:
                            topor_lvl += 1
                            coin -= 888
                            print("\nТопор улучшен 3lvl >>> 4lvl!")
                            print("- 888 монет")
                        else:
                            print("\nНедостаточно монет :(")
                elif action_master == "домой" or action_master == "Домой" or action_master == "Дом" or action_master == "дом":
                    loop = False
                else:
                    continue 

        else:
            break