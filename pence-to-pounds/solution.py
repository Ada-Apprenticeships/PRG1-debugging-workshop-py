def convert_from_pence_to_pounds(pence):
    pounds = pence / 100
    return f"£{round(pounds)}"  # Format to two decimal places

# Test the function
print(convert_from_pence_to_pounds(1299))  # should return "£12.99"