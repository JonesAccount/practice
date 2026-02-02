while True:
    try:
        action = int(input("[👤] "))
        print(self.__line)
        self.timer()
        if action == 1 or action == 0:
            break
        else:
            print("[🚫] Ответь нормально")
            print(self.__line)
            self.timer()
    except ValueError:
        print("[🚫] 1 или 2")
        print(self.__line)
        self.timer()