# 🧮 Count characters

## Problem statement

When working with strings, it's often necessary to count how many times a specific character appears within the text. This operation can be useful in various scenarios, such as analysing text content, validating input, or solving word puzzles. We need a function that can efficiently count the occurrences of a given character in a string, considering both uppercase and lowercase instances of the character as distinct.

## 📋 Function Specification

We're going to implement a function called `count_char` to solve this problem statement.

### Expected Behaviour

The function should:

1. Count the occurrences of the specified character in the given string
2. Return the count as an integer
3. Be case-sensitive (treat uppercase and lowercase characters as different)
4. Count all occurrences, including consecutive ones
5. Return 0 if the character is not found or if the string is empty

## Rules

- The function should be case-sensitive
- It should work with any printable character (letters, numbers, special characters)
- It should handle empty strings correctly
- If the character is not found in the string, it should return 0
- It should count all occurrences of the character, even if they are consecutive

### Function Signature

```python
def count_char(s: str, char: str) -> int:
```

### Parameters

- `s` (str): The string in which to search for the character
- `char` (str): A single character to search for

### Return Value

- (int): An integer representing the number of times the specified character appears in the string

## Examples

```python
count_char("hello", "l")  # should return 2
count_char("Mississippi", "s")  # should return 4
count_char("Mississippi", "p")  # should return 2
count_char("Cassandra", "a")  # should return 3
count_char("Cassandra", "A")  # should return 1
count_char("The quick brown fox jumps over the lazy dog", "o")  # should return 4
count_char("", "a")  # should return 0
count_char("No matches here", "z")  # should return 0
```
