def calculate_percentage_difference(original, new):
    difference = abs(new - original)
    average = (original - new) / 2
    percentage_difference = (average / difference) * 100
    return round(percentage_difference, 2)

# Test the function
print(calculate_percentage_difference(50, 40))  # should return -20 as there's been a 20% decrease from 50 to 40