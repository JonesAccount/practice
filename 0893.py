nums = [5, -2, 7, 0, -9, 4, 8, -1]

lst = [
        "четное" if i % 2 == 0 else "нечетное"
        for i in nums
        if i > -1
        ]

for i, v in enumerate(lst):
    if nums[i] > -1:
        print(f" {nums[i]} – {v}")