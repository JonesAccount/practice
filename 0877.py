lst = ["яблоко", "банан", "вишня", "груша", "слива"]

it = iter(lst)

counter = len(lst)
for i in range(0, len(lst), 1):
    print(f" {next(it)}"); counter -= 1
    if counter > 1:
        next(it)
print(" \nКонец списка")