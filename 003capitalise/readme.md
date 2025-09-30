# 🧵 Capitalise

## Problem Statement

You are tasked with implementing a function that modifies the capitalization of a given input string. The function should change the first character of the input string to uppercase while putting the rest of the string in lower case.

## Function Specification

We're implementing a function called `capitalise` to solve this problem statement.

## Expected Behaviour

The function should:

1. Accept a single string as input
2. Capitalize this first character
3. Put the **remaining characters in lower case**
4. Return the transformed string

### Function Signature

```python
def capitalise(s: str) -> str:
```

### Parameters

- `s` (str): The input string to be capitalized

### Return Value

- (str): The transformed string with the first character capitalized (if it's a letter)

## Examples

```python
capitalise("hello")  # should return "Hello"
capitalise("john")  # should return "John"
capitalise("WORLD")  # should return "World"
```
