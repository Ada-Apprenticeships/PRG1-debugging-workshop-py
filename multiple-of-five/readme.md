# 🧮 Is multiple of 5?

## Problem statement

In many programming scenarios, we need to determine if a number is divisible by another number without a remainder. A common case is checking if a number is a multiple of 5, which has various applications in mathematics and real-world problems. For example, this could be useful in problems involving currency (where the smallest unit is 5 cents), or in creating patterns or groupings based on multiples of 5. We need a function that can quickly and accurately determine whether a given integer is a multiple of 5.

## 📋 Function Specification

We're going to implement a function called `is_multiple_of_five` to solve this problem statement.

### Expected Behaviour

The function should:

1. Check if the input number is divisible by 5 without a remainder
2. Return `True` if it is divisible by 5, `False` otherwise

### Rules

- The function should work for any integer input (positive, negative, or zero)
- It should correctly identify multiples of 5 for both positive and negative numbers
- Zero should be considered a multiple of 5

### Function Signature

```python
def is_multiple_of_five(n: int) -> bool:
```

### Parameters

- `n` (int): An integer (positive, negative, or zero)

### Return Value

- (bool):
  - `True` if the input number is a multiple of 5
  - `False` if the input number is not a multiple of 5

## Examples

```python
is_multiple_of_five(0)  # should return True
is_multiple_of_five(5)  # should return True
is_multiple_of_five(10)  # should return True
is_multiple_of_five(15)  # should return True
is_multiple_of_five(100)  # should return True
is_multiple_of_five(-25)  # should return True
is_multiple_of_five(101)  # should return False
is_multiple_of_five(-7)  # should return False
is_multiple_of_five(3)  # should return False
```

## Buggy Implementation

Here's a buggy implementation of the `is_multiple_of_five` function:

```python
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
```

This implementation contains bugs that need to be fixed. Try running it and compare the output with the expected behavior described above. Can you identify and fix the issues?
