user = int(input("::"))
n = range(user)

it = iter(n)
for i in range(user):
    print(f" {next(it)}")