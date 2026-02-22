nums = 3, 8, 1, 6, 0, 7, 4
lst = [n * 5 for n in nums if n % 2 == 0]
tup = tuple(lst)
print(tup)
