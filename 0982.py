def func(*args):
    args = [i for i in args]
    return args[::-1]
    
lst = [1, 2, 3]
print(func(*lst))