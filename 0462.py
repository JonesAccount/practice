# Переменые
play_game = False
line = "-" * 30
dot = "•   •   •   •   •   •   •   •"
action_home = None
action_tree = None
action_shop = None
tree = 0
coin = 0

print("• ИГРА ДРОВОСЕК •", end="\n\n"); print(line)

while True:
    
    if play_game == True:
        print("\n", line, sep="")
        for i in range(5):
            print(dot)
        print(line)
    play_game = True
    
    print("|КОМАНДЫ|   |ДОМ|       id5725")
    print("• Рынок")
    print("• Лес", end="\n\n")
    
    print("|ИНВЕНТАРЬ|")
    print("• Топор ур. 1")
    print("• Дерево:", tree)
    print("• Монеты:", coin)
    
    print(line)
    
    loop_tree = True
    while loop_tree:
        action_home = input("|Действие >>> ")
        
        # это локация лес
        if action_home == "Лес" or action_home == "лес":
        
            print("\n", line, sep="")
            for i in range(5):
                print(dot)
            print(line)
        
            print("|КОМАНДЫ|   |ЛЕС|")
            print("• Рубить")
            print("• Домой")
        
            while loop_tree:
                action_tree = input("\n|Действие >>> ")
                if action_tree == "Рубить" or action_tree == "рубить" or action_tree == "Рубит" or action_tree == "рубит":
                    while loop_tree:
                        print("\n+ 1 дерево")
                        tree +=1
                        action_tree = input("\n|Действие >>> ")
                        if action_tree == "Рубить" or action_tree == "рубить" or action_tree == "Рубит" or action_tree == "рубит":
                            continue
                        elif action_tree == "домой" or action_tree == "Домой" or action_tree == "Дом" or action_tree == "дом":
                            loop_tree = False
                        else:
                            break
                else:
                    break
                    
        # это локация рынок
        if action_home == "Рынок" or action_home == "рынок":
        
            print("\n", line, sep="")
            for i in range(5):
                print(dot)
            print(line)
        
            print("|КОМАНДЫ|   |РЫНОК|")
            print("• Продать дерево")
            print("• Домой")
        
            while loop_tree:
                action_shop = input("\n|Действие >>> ")
                if action_shop == "Продать дерево" or action_shop == "продать дерево" or action_shop == "продать дерев":
                    if tree > 0:
                        while True:
                           print("\n+ " + str(tree * 5) + " монета (продано " + str(tree) + ")\n")
                           coin += tree
                           tree = 0
                           break
                    else:
                        print("\nНет дерево на продажу :(", end="\n\n")
                elif action_shop == "домой" or action_shop == "Домой" or action_shop == "Дом" or action_shop == "дом":
                    loop_tree = False
                else:
                    break
                
                
                
                if action_shop == "Рубить" or action_shop == "рубить" or action_shop  == "Рубит" or action_shop == "рубит":
                    while loop_tree:
                        print("\n+ 1 дерево")
                        tree +=1
                        action_shop = input("\n|Действие >>> ")
                        if action_shop == "Рубить" or action_shop == "рубить" or action_shop == "Рубит" or action_shop == "рубит":
                            continue
                        
                else:
                    break
        else:
            break