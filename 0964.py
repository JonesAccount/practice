def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs["word"])
    print(args[1] + kwargs["num"])

func(True, 3, 6.8, word = "hello", num = 56)