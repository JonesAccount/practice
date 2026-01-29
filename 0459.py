# Переменые
play_game = False
line = "-" * 30
dot = "•   •   •   •   •   •   •   •"
action_home = None
action_tree = None
loop_tree = None
tree = 0
coin = 0
a = True

print("• ИГРА ДРОВОСЕК •", end="\n\n"); print(line)

while True:
    
    if play_game == True:
        print("\n", line, sep="")
        for i in range(5):
            print(dot)
        print(line)
    play_game = True
    
    print("|МЕНЮ|\t\t\tid5725")
    print("• Продать дерево")
    print("• Улучшить топор")
    print("• Пойти в лес", end="\n\n")
    
    print("|ИНВЕНТАРЬ|")
    print("• Дерево:", tree)
    print("• Монеты:", coin)
    
    print(line)
    
    action_home = input("|Действие >>> ")
    
    if action_home == "Пойти в лес" or action_home == "пойти в лес":
        
        print("\n", line, sep="")
        for i in range(5):
            print(dot)
        print(line)
        
        print("|КОМАНДЫ|")
        print("• Рубить")
        print("• Домой")
        
        while a:
            action_tree = input("\n|Действие >>> ")
            if action_tree == "Рубить" or action_tree == "рубить" or action_tree == "Рубит" or action_tree == "рубит":
                loop_tree = True
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
                continue
                
                    
    else:
        continue