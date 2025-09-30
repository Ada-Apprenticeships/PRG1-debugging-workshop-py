def text_in_div(text, max_width):
    if max_width < 15:
        return "INVALID INPUT"
    formatted_text = ""
    while max_width < len(text):
        split_point = text.rindex("", max_width)
        formatted_text += text[:split_point] + "\n"
        text = text[split_point:]
    
    formatted_text = formatted_text + text
    return formatted_text

# Test the function
long_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec consectetur risus. Cras vel urna a tellus dapibus consequat. Duis bibendum tincidunt viverra. Phasellus dictum efficitur sem quis porttitor. Mauris luctus auctor diam id ultrices. Praesent laoreet in enim ut placerat. Praesent a facilisis turpis."
output = text_in_div(long_text, 50)
print(output)  # this isn't working correctly, check the output carefully against the expected behaviour