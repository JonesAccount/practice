class Car:
    d = "Машина едет"
    s = "Машина остановиласьь"
    
    def drive(self):
        print(self.d)
    
    def stop(self):
        print(self.s)

car = Car()
car.drive()
car.stop()