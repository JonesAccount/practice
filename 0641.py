class T:
    
    def f(self):
        self.x = 2
        self.y = 2
        print(pow(self.x, self.y))
        
    def init(self):
        try:
            self.x = int(input("::"))
            self.y = self.x
            print(self.x * self.y)
        except ValueError:
            print("Ошибка ввода")
        
t = T()
t.f()