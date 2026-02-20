nums = [[1,2], [3,4,5], [6]]

it = iter(nums)

for x in range(len(nums)):
    it = iter(nums[x])
    for i in range(len(nums[x])):
        num = next(it)
        if num % 2 == 0:
            print(f" {num}")