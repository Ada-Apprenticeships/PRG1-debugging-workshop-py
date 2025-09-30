
def find_century(year):
    century = (year - 1) // 100 + 1
    return str(century) + get_ordinal_suffix(century)

def get_ordinal_suffix(n):
    last_digit = n % 10

    if last_digit == 1:
        return "st"
    elif last_digit == 2:
        return "nd"
    elif last_digit == 3:
        return "rd"
    else:
        return "th"

# Hint: Start by calling find_century with an input of 1066. What should you expect to see?
print(find_century(1066))  # This will not give the correct output due to the bug