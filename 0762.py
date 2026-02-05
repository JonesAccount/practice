l = [6, 3, 8, 3, 2, 9]
l_clone = l[:]
l[1:-1:2] = [None, None]
print(l)

l_clone[3:] = ["Первый", "Второй", "Третий"]
l_clone.pop(2)
print(l_clone)