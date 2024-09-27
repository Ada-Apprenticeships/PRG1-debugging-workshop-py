# ➕ Increment

## Problem Statement

You are tasked with implementing a function that increases a given number by 1.

## 📋 Function Specification

We're implementing a function called `increment` to solve this problem statement.

### Expected Behaviour

The function should:

1. Accept a single number as input
2. Add 1 to the input number
3. Return the result of this addition

### Function Signature

```python
def increment(num: int) -> int:
```

### Parameters

- `num` (int): The input number to be incremented

### Return Value

- (int): The result of adding 1 to the input number

## Examples

```python
increment(5)  # should return 6
increment(-3)  # should return -2
increment(0)  # should return 1
increment(99)  # should return 100
increment(-1)  # should return 0
```

## Buggy Implementation

Here's a buggy implementation of the `increment` function:

```python
def increment(n):
    return n++

# Remember to check the expected behaviour of this program first
# Then call the function to check how it is actually working...

# Write some comments down below with your findings...
```

This implementation contains a bug that needs to be fixed. Try running it and compare the output with the expected behavior described above. Can you identify and fix the issue?

Note: The `n++` syntax used in the buggy implementation is not valid in Python. This is intentional and part of the bug that needs to be fixed. Consider how you would correctly increment a number in Python.
