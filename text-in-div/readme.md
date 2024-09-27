# 📜 Text in div

## Problem statement

This problem involves formatting some text to fit in a given width.

## 📋 Function Specification

We're implementing a function called `text_in_div` to solve this problem statement.

### Expected Behaviour

The function should:

1. Accept a string of text and a maximum line width as input
2. Split the input text into lines, ensuring that:
   - No line exceeds the specified maximum width
   - Words are not split across lines (break at spaces)
   - Lines are as long as possible within the width constraint (greedy approach)
3. Join the resulting lines with newline characters (\n)
4. Return the formatted text as a single string

### Function Signature

```python
def text_in_div(text: str, max_width: int) -> str:
```

### Parameters

- `text` (str): The input text to be formatted
- `max_width` (int): The maximum width of each line in characters

### Return Value

- (str): The formatted text with line breaks inserted

## Examples

```python
text_in_div("Ada National College for Digital Skills", 15)
# -> "Ada National\nCollege for\nDigital Skills"

text_in_div("Ada National College for Digital Skills", 20)
# -> "Ada National College\nfor Digital Skills"

text_in_div("Ada National College for Digital Skills", 30)
# -> "Ada National College for\nDigital Skills"

long_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec consectetur risus. Cras vel urna a tellus dapibus consequat. Duis bibendum tincidunt viverra. Phasellus dictum efficitur sem quis porttitor. Mauris luctus auctor diam id ultrices. Praesent laoreet in enim ut placerat. Praesent a facilisis turpis."

text_in_div(long_text, 30)
# -> "Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nAliquam nec consectetur risus.\nCras vel urna a tellus dapibus\nconsequat. Duis bibendum\ntincidunt viverra. Phasellus\ndictum efficitur sem quis\nporttitor. Mauris luctus\nauctor diam id ultrices.\nPraesent laoreet in enim ut\nplacerat. Praesent a facilisis\nturpis."

text_in_div(long_text, 50)
# -> "Lorem ipsum dolor sit amet, consectetur adipiscing\nelit. Aliquam nec consectetur risus. Cras vel urna\na tellus dapibus consequat. Duis bibendum\ntincidunt viverra. Phasellus dictum efficitur sem\nquis porttitor. Mauris luctus auctor diam id\nultrices. Praesent laoreet in enim ut placerat.\nPraesent a facilisis turpis."
```

## Buggy Implementation

Here's a buggy implementation of the `text_in_div` function:

```python
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
```

This implementation contains bugs that need to be fixed. Try running it and compare the output with the expected behavior described above. Can you identify and fix the issues?
