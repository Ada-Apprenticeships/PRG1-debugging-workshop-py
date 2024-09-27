# findClosingParenthesis Function

## Problem statement

We need to find the index of the closing parenthesis that matches the opening parenthesis at a given position in a string. This function is useful in parsing expressions or code snippets that contain nested parentheses.

## 📋 Function specification

We're implementing a function called `findClosingParenthesis` to solve this problem statement.

### Expected Behaviour

- The function should return the correct index of the matching closing parenthesis.
- It should handle nested parentheses correctly.
- If the `openPos` doesn't point to an opening parenthesis, it should return -1.
- If there's no matching closing parenthesis, it should return -1.
- The function should ignore any characters that are not parentheses.

### Function Signature

```javascript
function findClosingParenthesis(str, openPos)
```

### Parameters

- `str` (string): The input string containing parentheses.
- `openPos` (number): The index of the opening parenthesis in the string.

### Return Value

- (number): Returns the index of the matching closing parenthesis.
- Returns -1 if no matching closing parenthesis is found or if the input is invalid.

## Examples

```javascript
findClosingParenthesis('');
  --> -1
```

```javascript
findClosingParenthesis('hello');
  --> -1
```

```javascript
findClosingParenthesis('(hello)', 1);
  --> 6
```

```javascript
findClosingParenthesis('Hello, (world). (Something Else).', 2);
  --> 31
```

```javascript
findClosingParenthesis('Hello, (world, (foo) bar (something) else), foo (bar) cat', 3);
  --> 35
```
