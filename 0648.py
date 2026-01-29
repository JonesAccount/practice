# сортировка
# модуль
# удалить буквы
# удалить дубдикаты
# перевернуть список
# в конце преобразовать в кортеж
from random import randint as r

class Type:
    lst = None
    
    def init(self, lst):
        print("Запуск...\n")
        print(f"Оригинал:\n{lst}")
        self.lst = lst
        self.sort_f()
    
    def sort_f(self):
        self.lst.sort()
        print(f"\nСортировка:\n{self.lst}")
        self.modul_f()
    
    def modul_f(self):
        for i in range(len(lst)):
            self.lst[i] = abs(self.lst[i])
        print(f"\nМодуль:\n{self.lst}")
        self.dubl_f()
    
    def dubl_f(self):
        mno = set(self.lst)
        self.lst.clear()
        for i in range(len(mno)):
            el = mno.pop()
            self.lst.append(el)
        print(f"\nУдаление дубликатов:\n{self.lst}")
        self.rev_f()
        
    def rev_f(self):
        self.lst.reverse()
        print(f"\nПеревернуть список:\nВерсия 1: {self.lst}")
        self.rev_f2()
        
    def rev_f2(self):
        print(f"Версия 2: {self.lst[::-1]}")
        self.tup_f()
            
    def tup_f(self):
        corte = tuple(self.lst)
        print(f"\nКортеж:\n{corte}")

lst = []
for i in range(8):
    lst.append(r(-5, 9))
    
type = Type(lst)