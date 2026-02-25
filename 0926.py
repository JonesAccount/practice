class Character:
    def init(self, name, age):
        # персонаж
        self.name: str = name
        self.age: int = age
        
        # состояние персонажа
        self.hungry: int = 5
        self.happiness: int = 5
        self.energy: int = 5
        self.cleanliness: int = 5
        

class CreateCharacter:
    def init(self):
        self.name = None
        self.age = None
        
    def get_name(self):
        self.name = input("Имя: ")
        return self.name
    
    def get_age(self):
        while True:
            try:
                self.age = int(input("Возвраст: "))
                break
            except ValueError:
                print("Нужно ввести возраст")
        return self.age
                

def main():
    creator = CreateCharacter()
    name = creator.get_name()
    age = creator.get_age()
    char = Character(name, age)
    while True:
        print(f"""🌸{char.name.capitalize()} | Возраст: {char.age} лет | Рост: 105 см.
=====================================
✨ Состояние:

Сытость: {char.hungry}/10     Счастье: {char.happiness}/10
Энергия: {char.energy}/10     Чистота: {char.cleanliness}/10
=====================================
❔ Что делать:

1. Покормить      2. Поиграть
3. Уложить спать  4. Отлучится
-------------------------------------""")
        action = input("> ")

main()