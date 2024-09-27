def convert_to_12_hour_clock(time):
    hours = int(time[:2])
    minutes = time[-2:]
    if hours > 12:
        return f"{hours - 12}:{minutes} PM"
    else:
        return f"{hours}:{minutes} AM"

# Hint: Try calling the function with an input of '12:05'
print(convert_to_12_hour_clock('12:00'))