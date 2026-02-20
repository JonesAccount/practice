lst = ["яблоко", "банан", "вишня", "груша", "слива"]

it = iter(lst)

try:
    while 1:
        print(f" {next(it)}"); next(it)
except:
    print(" \nКонец")