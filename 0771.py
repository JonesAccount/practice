from random import randint as r

a, b, c = r(0, 9), r(0, 9), r(0, 9)
print(a, b, c, sep="|")

res = (a if a > b else b) if b > c else (c if c > a else a)

result = True if res == max(a, b, c) else False

print(res)
print(result)
    
# a-b|b-c|a-c