# 🪙 Pence to pounds

## Problem statement

In the United Kingdom and some other countries, the currency is divided into pounds (£) and pence (p), where 100 pence make up one pound. When dealing with financial calculations or displaying prices, it's often necessary to convert an amount given entirely in pence to its equivalent in pounds and pence. This conversion needs to accurately represent the amount with pounds as the whole number part and pence as the decimal part, formatted correctly as currency.

## 📋 Function Specification

We're implementing a function called `convert_from_pence_to_pounds` to solve this problem statement.

### Expected Behaviour

The function should:

1. Convert the input amount from pence to pounds
2. Format the result as a string representing currency in pounds and pence
3. Return the formatted string

### Rules

- The return string must start with the pound symbol (£)
- It should show the number of whole pounds
- Use a decimal point to separate pounds and pence
- Always show two decimal places for the pence, even if they're zero
- Correctly handle amounts less than one pound
- The function should work for any non-negative integer input

### Function Signature

```python
def convert_from_pence_to_pounds(pence: int) -> str:
```

### Parameters

- `pence` (int): An integer representing the amount in pence

### Return Value

- (str): A string representing the amount in pounds and pence, formatted as currency

## Examples

```python
convert_from_pence_to_pounds(1299)  # should return "£12.99"
convert_from_pence_to_pounds(700)  # should return "£7.00"
convert_from_pence_to_pounds(50)  # should return "£0.50"
convert_from_pence_to_pounds(2000)  # should return "£20.00"
convert_from_pence_to_pounds(199)  # should return "£1.99"
convert_from_pence_to_pounds(1)  # should return "£0.01"
convert_from_pence_to_pounds(0)  # should return "£0.00"
```

## Buggy Implementation

Here's a buggy implementation of the `convert_from_pence_to_pounds` function:

```python
def convert_from_pence_to_pounds(pence):
    pounds = pence / 100
    return f"£{round(pounds)}"  # Format to two decimal places

# Test the function
print(convert_from_pence_to_pounds(1299))  # should return "£12.99"
```

This implementation contains bugs that need to be fixed. Try running it and compare the output with the expected behavior described above. Can you identify and fix the issues?
