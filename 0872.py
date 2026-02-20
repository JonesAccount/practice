t = "Data"

counter: int = 5
while counter != 0:
    it = iter(t)
    for i in range(len(t)):
        print(f" {next(it)}")
    print()
    counter -= 1