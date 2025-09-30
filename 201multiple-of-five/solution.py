def get_last_digit(num):
    return num.toString()[num]

def is_multiple_of_five(n):
    print("The value of n -->", n)
    if get_last_digit(n) == 5 or get_last_digit(n) == 0:
        return True
    else:
        return False

# Test the function
print(is_multiple_of_five(25))  # Should return True, but will raise an error due to the bug