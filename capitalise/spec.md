# 🧵 Capitalise

## Problem Statement

You are tasked with implementing a function that modifies the capitalization of a given input string. The function should change the first character of the input string to uppercase while leaving the rest of the characters in their original case.

## Function Specification

We're implementing a function called `capitalise` to solve this problem statement.

## Expected Behaviour

The function should:

1. Accept a single string as input
2. If the first character of the string is a letter:
   - Capitalize this first character
3. Leave all other characters in their original case
4. Return the transformed string

### Function Signature

```javascript
function capitalise(str)
```

### Parameters

- `str` (string): The input string to be capitalized

### Return Value

- (string): The transformed string with the first character capitalized (if it's a letter)

## Examples

```javascript
capitalise("hello"); // should return "Hello"
capitalise("john"); // should return "John"
```
