def count_char(string, char):
    i = 0
    count = 0
    while i < len(char):
        if string[i] == char:
            count += 1
        i += 1
    return count

# Test the function
print(count_char("aaaabbbcc", "b"))  # should return 3