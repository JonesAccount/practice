lst = [4, True, lambda w="word": len(w) ** 2, "Python", (1,)]
    
p = print
p(lst)

p()
p(lst[2]())