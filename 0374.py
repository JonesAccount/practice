class Planet:
    def __init__(self, earth, jupiter, mars, venus):
        self.earth = earth
        self.jupiter = jupiter
        self.mars = mars
        self.venus = venus
        
    def habitability_analysis(self):
        print("\n|АНАЛИЗ ПЛАНЕТ|")
        print(self.earth + ": обитаемая")
        print(self.jupiter + ": не обитаемый")
        print(self.mars + ": пригодно для терроформации")
        print(self.venus + ": не обитаемая")

info_planet = Planet("Земля", "Юпитер", "Марс", "Венера")

print("Мои любимые планеты: " + info_planet.earth + ", " + info_planet.jupiter + ", " + info_planet.mars + ", " + info_planet.venus)

info_planet.habitability_analysis()

# В объектно-ориентированном программировании — переменная, описание которой создает программист при создании класса. Все данные объекта хранятся в его полях. Доступ к полям осуществляется по их имени. В нашем случае атрибуты: earth, jupiter, mars, venus