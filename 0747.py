# with open('0745.txt') as file:
#     print(file.read())

lst = ["Python", "Java", "C#"]

try:
    print("start")
    print("-" * 40)

    with open('0745.txt', 'a+') as file:
        file.seek(0)
        file.writelines(lst)
        print(file.read())

    print("-" * 40)
except:
    print("idk but error")
else:
    print(file.closed)
finally:
    print("Progred")