class Lamp:
    is_on = False
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False
    
    def islamp(self):
        print("Лампа включена") if self.is_on == True else print("Лампа выключена")
        
l = Lamp()
l.islamp()

l.turn_on()
l.islamp()

l.turn_off()
l.islamp()