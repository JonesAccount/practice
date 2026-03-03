def digit_sum(n):
    if n <= 1:
        return n
    else:
        return n + digit_sum(n - 1)
    
    
print(digit_sum(5))