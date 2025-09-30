# 🌡️ Temperature Converter

## Problem Statement

Temperature is commonly measured in two different scales: Celsius and Fahrenheit. Many countries use Celsius for everyday temperature measurements, while others, like the United States, primarily use Fahrenheit. This difference can lead to confusion when sharing temperature information across different regions or in international contexts. We need a way to easily convert temperatures between these two scales to facilitate clear communication and understanding.

## 📋 Function Specification

We're going to implement a function called `convert_temperature` to solve this problem statement.

### Expected Behaviour

The function should convert the input temperature from one unit to another, adhering to the following rules:

1. It should be able to convert from Celsius to Fahrenheit and vice versa.
2. The conversion should use the correct formula for each direction:
   - Celsius to Fahrenheit: (C * 9/5) + 32
   - Fahrenheit to Celsius: (F - 32) * 5/9
3. The result should be rounded to two decimal places.
4. If the input and output units are the same, it should return the input temperature (rounded to two decimal places).
5. The function should raise a ValueError for unsupported unit conversions.

### Function Signature

```python
def convert_temperature(temperature: float, from_unit: str, to_unit: str) -> float:
```

### Parameters

- `temperature` (float): The temperature value to be converted
- `from_unit` (str): The unit of the input temperature ('C' for Celsius, 'F' for Fahrenheit)
- `to_unit` (str): The unit to convert the temperature to ('C' for Celsius, 'F' for Fahrenheit)

### Return Value

- (float): The converted temperature, rounded to two decimal places

## Examples

```python
convert_temperature(0, "C", "F")  # should return 32.0
convert_temperature(100, "C", "F")  # should return 212.0
convert_temperature(32, "F", "C")  # should return 0.0
convert_temperature(98.6, "F", "C")  # should return 37.0
convert_temperature(25, "C", "C")  # should return 25.0
convert_temperature(-40, "C", "F")  # should return -40.0
convert_temperature(-40, "F", "C")  # should return -40.0

# Error case
convert_temperature(20, "K", "C")  # should raise a ValueError
```
