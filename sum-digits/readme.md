# 🧮 Sum digits

## Problem statement

Let's consider a number like 2024. Its digit sum is the sum of each digit in the number. In this case, the digit sum would be 2 + 0 + 2 + 4 to get 8. We need to find a way to calculate the digit sum for any number.

## 📋 Function Specification

We're implementing a function called `sum_digits` to solve this problem statement.

### Expected Behaviour

The function should:

1. Take a positive integer as input
2. Calculate the sum of all individual digits in the number
3. Return the resulting sum

### Rules

- The function should work for any positive integer input
- Zero should be handled correctly (summing to 0)
- The function should consider each digit individually, not the place value

### Function Signature

```python
def sum_digits(num: int) -> int:
```

### Parameters

- `num` (int): A positive integer whose digits are to be summed

### Return Value

- (int): The sum of all digits in the input number

## Examples

```python
sum_digits(103)  # should return 4 (because 1 + 0 + 3 = 4)
sum_digits(257)  # should return 14 (because 2 + 5 + 7 = 14)
sum_digits(1000)  # should return 1 (because 1 + 0 + 0 + 0 = 1)
sum_digits(0)  # should return 0
sum_digits(9)  # should return 9
sum_digits(12345)  # should return 15 (because 1 + 2 + 3 + 4 + 5 = 15)
```
