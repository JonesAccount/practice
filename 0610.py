nums = [5, -2, 7, 3, -1]
print(f"Исходник: {nums}")

l = lambda x: pow(abs(x), 2)
    
sum = 0
for i in range(len(nums)):
    nums[i] = l(nums[i])
    sum += nums[i]
    
print(f"Новый список: {nums}")
print(f"Сумма всех чисел: {sum}")