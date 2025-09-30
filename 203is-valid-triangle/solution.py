def is_valid_triangle(a, b, c):
    # Check if all sides are positive
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Check the triangle inequality
    if a + b > c and b + c > a and c + a > b:
        return True

    return False

# Test cases
print(is_valid_triangle(3, 4, 5))  # Should return True
print(is_valid_triangle(1, 1, 3))  # Should return False
print(is_valid_triangle(5, 10, 25))  # Should return False
print(is_valid_triangle(-1, 2, 3))  # Should return False