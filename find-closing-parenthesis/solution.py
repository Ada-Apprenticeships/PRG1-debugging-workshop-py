def find_closing_parenthesis(s, open_pos):
    if s[open_pos] != "(":
        return -1

    count = 0
    i = open_pos

    while i < len(s):
        if s[i] == "(":
            count += 1
        elif s[i] == ")":
            count -= 1

        if count == 0:
            return i

        i += 1

    return -1

print(find_closing_parenthesis('Hello, (world). (Something Else).', 2)) # --> 31

