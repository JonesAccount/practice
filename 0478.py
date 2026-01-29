# глобальные переменные
coin = None
iron = None

def home(): # локация «дом»
    print("────── ТЕЛЕЖКА ──────"); print("1) Деревянная кирка"); print("2) Железо: 0"); print("3) Уголь: 0"); print("4) Медь: 0")
    print("\n────── КОМАНДЫ ──────"); print("1) Шахта"); print("2) Продать руды"); print("────────────────────")
    action = input("\nДействие: ")
    if action == "шахта":
        mine()

def mine(): # локация «шахта»
    print("|КОМАНДЫ|"); print("• Копать"); print("• Домой")
    action = input("\nТвое действие: ")
    if action == "дом":
        home()
    
home()