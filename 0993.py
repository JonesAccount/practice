nums = [123, 45, 6]
new = list()

res = 0
for n in nums:
    num = str(n)
    for i in num:
        res += int(i)
    new.append(res)
    res = 0
    
print(nums)
print(new)