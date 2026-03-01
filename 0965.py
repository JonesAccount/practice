from random import randint, choice

mixed = [
    "apple", 42, True, 3.14, None,
    "banana", False, 7, "cherry", 0,
    99, "dog", True, "cat", 2.718,
    None, "orange", 15, False, "grape",
    "kiwi", 1, True, 100, "mango",
    0.5, "pear", None, False, 8,
    "peach", True, "plum", 12, 3.1415,
    "melon", None, 77, False, "berry",
    9, "lemon", True, 0, "lime",
    42, "apricot", None, False, "fig",
    "red", 1, True, 0.5, None,
    "blue", False, 77, "green", 3.14,
    "yellow", None, 9, True, "purple",
    100, "pink", False, 2.718, "brown",
    None, "black", 8, True, "white",
    42, "gray", False, 0, "cyan",
    "magenta", None, 66, True, "lime",
    13.5, "teal", False, 5, "navy",
    None, "maroon", True, 7, "olive",
    99, False, "beige", 0.01, "gold",
    "sun", 88, False, 2.5, None,
    "moon", True, 13, "star", 0.99,
    7, "cloud", None, True, "rain",
    101, False, "wind", 3.333, "snow",
    None, "storm", 21, True, "fog",
    0, "lightning", False, 55, "thunder",
    6.28, None, "hurricane", True, 17,
    "tornado", False, 9, "drizzle", 42,
    "mist", None, True, 11, "dew",
    0.1, False, "hail", 33, "frost"
]

d = {choice((i for i in mixed if isinstance(i, str))): choice(mixed) for i in range(randint(1, 10))}
    
l = (choice(mixed) for i in range(randint(1, 10)))
    
    
def func(*args, **kwargs) -> str:
    """
    фанкшин аркс кваркс
    """
    for k, v in kwargs.items():
        print(f"{k}: {v}")


print(d)