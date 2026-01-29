# Найдите три ключа с самыми высокими значениями в словаре

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
lst = []
num1, num2, num3 = None, None, None

for i in my_dict.values():
    lst.append(i)
    
lst.sort()
print(lst)
num1 = lst[-1]
lst.pop(-1)
num2 = lst[-1]
lst.pop(-1)
num3 = lst[-1]

print(f"\n1. {num1}\n2. {num2}\n3. {num3}")