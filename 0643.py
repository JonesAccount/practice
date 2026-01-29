from cowsay import cow

class D:
    word = None
    
    def init(self, x, y):
        print(x)
        self.word = y
    
    def f(self, x = None):
        cow(self.word)
    
d = D("Запуск..\n", "Бобркурва, я пердоле")
d.f()