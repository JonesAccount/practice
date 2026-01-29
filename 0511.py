def f1():
    num = 5
    def f2():
        nonlocal num
        result = num * num
        return result
    return f2()
    
print(f1())