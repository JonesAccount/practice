it = iter(range(int(input("::"))))

try:
    while 1:
        print(f" {next(it)}")
except:
    print(" Конец")