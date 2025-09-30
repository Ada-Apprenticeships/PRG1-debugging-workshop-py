def sum_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num -= 1
    return total

# Test the function
print(sum_digits(12345))  # Should return 15