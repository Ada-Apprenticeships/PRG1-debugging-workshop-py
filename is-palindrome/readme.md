# isPalindrome Function

A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, disregarding spaces, punctuation, and capitalization. We need to determine whether a given string is a palindrome.

## 📋 Function specification

We're implementing a function called `is_palindrome` to solve this problem statement.

### Expected Behaviour

- The function should return `True` for palindromes and `False` for non-palindromes.
- The function should ignore spaces, punctuation, and capitalization.
- An empty string should be considered a palindrome.

### Function Signature

```python
def is_palindrome(s: str) -> bool:
```

### Parameters

- `s` (str): The input string to check for palindrome property.

### Return Value

- (bool): Returns `True` if the input string is a palindrome, `False` otherwise.

## Use cases

```python
is_palindrome("racecar")  # should return True
is_palindrome("hello")  # should return False
is_palindrome("A man a plan a canal Panama")  # should return True
is_palindrome("race a car")  # should return False
is_palindrome("")  # should return True
```

## Buggy Implementation

Here's a buggy implementation of the `is_palindrome` function:

```python
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right += 1

    return True

print(is_palindrome("racecar"))  # should return True
```

This implementation contains bugs that need to be fixed. Try running it and compare the output with the expected behavior described above. Can you identify and fix the issues?
