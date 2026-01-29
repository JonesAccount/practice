class Car:
    brand = None
    dic = None
    
    def fac(self, price):
        self.dic[self.brand] = price
        print(self.dic[self.brand])

car = Car()
car.brand = "Tesla"
car.dic = {}
car.fac(5000)