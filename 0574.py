l = []

while not False:
    var = input("Число: ")
    if var == "stop":
        break
    else:
        l.append(int(var))
        
print(l)
word = " ".join(l)
print(word.find("5"))