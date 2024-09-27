# find_closing_parenthesis

## Problem statement

Create a function that takes a string containing at least one or more pairs of matched parentheses and a number, n, which represents the nth opening parenthesis.

Your function should find the index position of the closing parenthesis that matches the nth opening parenthesis.

The parentheses will always be matched and valid, and you will only ever get regular parentheses () and no brackets etc.

If the string is empty or no number is given, you should return -1

## 📋 Function specification

We're implementing a function called `find_closing_parenthesis` to solve this problem statement.

### Expected Behaviour

- The function should return the correct index of the matching closing parenthesis.
- It should handle nested parentheses correctly.
- If the `open_pos` doesn't point to an opening parenthesis, it should return -1.
- If there's no matching closing parenthesis, it should return -1.
- The function should ignore any characters that are not parentheses.

### Function Signature

```python
def find_closing_parenthesis(s: str, n: int) -> int:
```

### Parameters

- `s` (str): The input string containing parentheses.
- `n` (int): The value that tells us which opening parenthesis to target.

### Return Value

- (int): Returns the index of the matching closing parenthesis.
- Returns -1 if no matching closing parenthesis is found or if the input is invalid.

## Examples

```python
find_closing_parenthesis('', 0)
  # --> -1

find_closing_parenthesis('hello', 0)
  # --> -1

find_closing_parenthesis('(hello)', 0)
  # --> 6

find_closing_parenthesis('Hello, (world). (Something Else).', 7)
  # --> 13

find_closing_parenthesis('Hello, (world). (Something Else).', 2)
  # --> 31
```

## Buggy Implementation

Here's a buggy implementation of the `find_closing_parenthesis` function:

```python
def find_closing_parenthesis(s, open_pos):
    if s[open_pos] != "(":
        return -1

    count = 0
    i = open_pos

    while i < len(s):
        if s[i] == "(":
            count += 1
        elif s[i] == ")":
            count -= 1

        if count == 0:
            return i

        i += 1

    return -1

print(find_closing_parenthesis("Hello, (world). (Something Else).", 7))  # should return 13
```

This implementation contains a subtle bug that needs to be fixed. Try running it and compare the output with the expected behavior described above. Can you identify and fix the issue?
