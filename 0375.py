class Technology:
    def __init__(self, seeds, glass):
        self.seeds = seeds
        self.glass = glass
        
    def calculator(self):
        print(self.seeds * self.glass)

math = Technology(150, 8)

math.calculator()
