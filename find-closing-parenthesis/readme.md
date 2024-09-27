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
- If the `n` doesn't point to an opening parenthesis, it should return -1.
- If there's no matching closing parenthesis, it should return -1.
- The function should ignore any characters that are not parentheses.

### Function Signature

```python
def find_closing_parenthesis(s: str, n: int) -> int:
```

### Parameters

- `s` (str): The input string containing parentheses.
- `n` (int): Which opening parenthesis to start at.

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
