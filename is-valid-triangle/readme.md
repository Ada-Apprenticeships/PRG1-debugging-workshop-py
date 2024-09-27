# 📐 Is it a valid triangle?

## Problem statement

In geometry, a triangle is a shape with three sides. However, not every combination of three lengths can form a valid triangle. A fundamental rule in triangle construction is that the sum of the lengths of any two sides must be greater than the length of the remaining side. This rule ensures that the triangle can be closed. We need a function that can determine whether three given lengths can form a valid triangle. This function could be useful in various geometric applications, including computer graphics, game development, or mathematical problem-solving.

## 📋 Function Specification

We're going to implement a function called `is_valid_triangle` to solve this problem statement.

### Function Signature

```python
def is_valid_triangle(a: float, b: float, c: float) -> bool:
```

### Parameters

- `a` (float): Length of the first side of the triangle
- `b` (float): Length of the second side of the triangle
- `c` (float): Length of the third side of the triangle

### Return Value

- (bool):
  - `True` if the three lengths can form a valid triangle
  - `False` if the three lengths cannot form a valid triangle

### Expected Behaviour

The function should:

1. Check if all three input values are positive numbers greater than zero
2. Verify that the triangle inequality theorem is satisfied for all three combinations of sides:
   - a + b > c
   - b + c > a
   - c + a > b
3. Return `True` if both conditions above are met, `False` otherwise

## Examples

```python
is_valid_triangle(3, 4, 5)  # should return True
is_valid_triangle(5, 12, 13)  # should return True
is_valid_triangle(1, 1, 1)  # should return True
is_valid_triangle(1, 2, 3)  # should return False
is_valid_triangle(2, 4, 2)  # should return False
is_valid_triangle(7, 3, 2)  # should return False
is_valid_triangle(0, 0, 0)  # should return False
is_valid_triangle(-1, 2, 3)  # should return False
```

## Additional Considerations

- The function should work with both integer and floating-point numbers
- The function should return `False` for any invalid inputs (negative numbers or zero)
- This function helps reinforce understanding of geometric principles and conditional logic
- It's a good exercise for students learning about both mathematics and programming
