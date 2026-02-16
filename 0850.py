n = int(input("Число: "))

res = 1
for x in range(1, n + 1):
    res *= x
    
print(f"{n}! = {res}")