word = input("::")

countP = 0
countL = 0
for i in word:
    if i.isupper():
        countP += 1
    elif i.islower():
        countL += 1
        
print(countP, countL)