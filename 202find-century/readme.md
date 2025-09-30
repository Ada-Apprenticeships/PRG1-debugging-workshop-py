# 📆 Find century

## Problem statement

We need to find the century for a given year with the appropriate ordinal suffix (e.g., "11th", "21st").

## 📋 Function Signature

We're going to implement a function called `find_century` to solve this problem statement.

### Expected behaviour

1. The century is calculated by dividing the year minus 1 by 100 and rounding down, then adding 1.
2. The appropriate ordinal suffix is determined based on the last digit of the century.
3. The century number and its suffix are combined and returned.

```python
def find_century(year: int) -> str:
```

### Parameters

- `year` (int): The year for which to find the century

### Return Value

- (str): The century with its ordinal suffix

## Helper Function: `get_ordinal_suffix`

This function determines the appropriate ordinal suffix for a number.

```python
def get_ordinal_suffix(n: int) -> str:
```

### Parameters

- `n` (int): The number for which to determine the ordinal suffix

### Return Value

- (str): The ordinal suffix ('st', 'nd', 'rd', or 'th')

## Examples

```python
find_century(101)  # Should return "2nd"
find_century(300)  # Should return "3rd"
find_century(1066)  # Should return "11th"
find_century(1776)  # Should return "18th"
find_century(2023)  # Should return "21st"
```

## Edge Cases

- Years from 1 to 100 are considered part of the 1st century.
- The function assumes positive integer inputs for years.

## Notes

- The function correctly handles the special cases for 11th, 12th, and 13th centuries, which all use the 'th' suffix regardless of their last digit.

## Hint for Testing

Start by calling `find_century` with an input of 1066. You should expect to see "11th" as the result.

## Possible Extensions

- Add input validation to ensure the year is a positive integer.
- Extend the function to handle BC/BCE years.
- Create a version that works with different calendar systems.
