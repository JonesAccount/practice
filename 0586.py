def is_even(num):
    result = None
    if num % 2 == 0:
        result = True
    else:
        result = False
    return result

print(is_even(4))
print(is_even(7))