class Timer:
    _seconds = 0
    
    def add(self):
        self._seconds += 1
        
    def subtract(self):
        if self._seconds > 0:
            self._seconds -= 1
            
    def reset(self):
        self._seconds = 0
        
    def get_time(self):
        return f"Секунды: {self._seconds}" if self._seconds > 0 else "Секунды: 0"
        
t = Timer()
t.add()
t.add()
t.subtract()
t.add()
print(t.get_time())
t.reset()
print(t.get_time())