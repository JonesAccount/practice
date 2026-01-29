def f1():
    num = 1013
    def f2():
        def f3():
            nonlocal num
            num *= 2
            return num
        return f3()
    return f2()

print(str(f1()) + " год.")