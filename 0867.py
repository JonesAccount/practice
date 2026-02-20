with open("db.txt", "a+", encoding="UTF-8") as fl:
    
    
    while True:
        nick = input("Ник: ")
        fl.seek(len(fl.read()) - 3)
        if nick not in fl:
            fl.write(nick)
        else:
            if nick not in fl:
                fl.write(nick)
                
                
        fl.seek(0)
        print(fl.tell())
        print(fl.readlines())