try:
    file = open("0730.txt","r")
    try:
        print(file.read())
        int("idk")
    finally:
        file.close()
except FileNotFoundError:
    print("File not found")
except:
    print("idk but error")