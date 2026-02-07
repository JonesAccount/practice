def f1(x):
    x = x * 5
    def f2():
        nonlocal x
        x += x
        print(x)
    return f2
        
func_two = f1(5)
func_one = f1(3)

func_one()
func_two()