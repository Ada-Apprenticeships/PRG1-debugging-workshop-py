# Find the closing parenthesis

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
def find_closing_parenthesis(str: str, n: int) -> int:
```

### Parameters

- `str` (string): The input string containing parentheses.
- `n` (number): An integer representing which opening parenthesis to match, counting from left to right. For example, n=1 means find the match for the first opening parenthesis, n=2 for the second, and so on.

### Return Value

- (int): Returns the index of the matching closing parenthesis.
- Returns -1 if no matching closing parenthesis is found or if the input is invalid.

## Examples

```python
find_closing_parenthesis("(hello)", 1)
# should return 6
```

```python
find_closing_parenthesis("Hello, (world). (Something Else).", 2)
# should return 31
```

```python
find_closing_parenthesis("Hello, (world, (foo) bar (something) else), foo (bar) cat",3)
# should return 35
```
