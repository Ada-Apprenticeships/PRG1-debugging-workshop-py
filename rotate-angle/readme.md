## 🔄 Rotate angle

## Problem statement

In many applications involving geometry, graphics, or physics, we often need to rotate angles. An angle is typically measured in degrees, with a full circle being 360 degrees. When we rotate an angle, we add or subtract degrees, but we need to ensure that the result always falls within the range of 0 to 359 degrees (inclusive). If the rotation results in an angle outside this range, we need to wrap it around, similar to how a clock face wraps around after 12 hours. We need a function that can perform this rotation calculation, handling both positive and negative rotations, and ensuring the result is always a valid angle between 0 and 359 degrees.

## 📋 Function Specification

We're going to implement a function called `rotate_angle_by_degrees` to solve this problem statement.

### Expected Behaviour

The function should:

1. Take the initial angle and apply the specified rotation
2. Normalize the result to fall between 0 and 359 degrees (inclusive)
3. Return the new angle as an integer

## Rules

- The initial angle should always be between 0 and 359 degrees (inclusive)
- The rotation can be any integer (positive, negative, or zero)
- Positive rotations move clockwise, negative rotations move counterclockwise
- The result should always be normalized to fall between 0 and 359 degrees (inclusive)
- Full rotations (multiples of 360 degrees) should result in the same angle as the starting angle

### Function Signature

```python
def rotate_angle_by_degrees(initial_angle: int, rotation: int) -> int:
```

### Parameters

- `initial_angle` (int): The initial angle in degrees (an integer between 0 and 359, inclusive)
- `rotation` (int): The rotation in degrees (an integer, positive or negative)

### Return Value

- (int): The new angle after rotation, as an integer between 0 and 359 (inclusive)

## Examples

```python
rotate_angle_by_degrees(45, 45)  # should return 90
rotate_angle_by_degrees(350, 15)  # should return 5
rotate_angle_by_degrees(0, 360)  # should return 0
rotate_angle_by_degrees(180, -180)  # should return 0
rotate_angle_by_degrees(270, 180)  # should return 90
rotate_angle_by_degrees(90, -100)  # should return 350
rotate_angle_by_degrees(0, 720)  # should return 0
rotate_angle_by_degrees(45, -405)  # should return 0
```

## Buggy Implementation

Here's a buggy implementation of the `rotate_angle_by_degrees` function:

```python
def rotate_angle_by_degrees(initial_angle, rotation):
    # Calculate the new angle
    new_angle = initial_angle + (rotation % 360)

    return new_angle

# Test the function
print(rotate_angle_by_degrees(350, 15))  # Should return 5, but won't due to the bug
```

This implementation contains a bug that needs to be fixed. Try running it and compare the output with the expected behavior described above. Can you identify and fix the issue?
