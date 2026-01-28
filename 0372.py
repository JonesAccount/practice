information1 = input()
information2 = input()

class Info:
    def __init__(self, argument1, argument2):
        self.argument1 = argument1
        self.argument2 = argument2

my_info = Info(information1, information2)

print("First info: " + my_info.argument1)
print("Second info: " + my_info.argument2)

# self — это ссылка на текущий экземпляр класса. Это способ обращения к атрибутам и методам класса изнутри самого класса.