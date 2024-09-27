def convert_temperature(temperature, to_unit, from_unit):
    # Check if the units are the same
    if from_unit == to_unit:
        return round(temperature, 2)

    result = 0

    # Convert based on the from_unit
    if from_unit == "C" and to_unit == "F":
        result = (temperature * 9) / 5 + 32
    elif from_unit == "F" and to_unit == "C":
        result = ((temperature - 32) * 5) / 9
    else:
        raise ValueError("Unsupported unit conversion")

    # Round to two decimal places
    return round(result, 2)

# Test cases
print(convert_temperature(0, "C", "F"))  # Should output: 32.0
print(convert_temperature(100, "C", "F"))  # Should output: 212.0
print(convert_temperature(32, "F", "C"))  # Should output: 0.0
print(convert_temperature(98.6, "F", "C"))  # Should output: 37.0