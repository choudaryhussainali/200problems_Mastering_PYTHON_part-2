# Exercise 30: Reverse Numeric Strings

# Take 5 inputs (numbers or numeric strings). For each:

# Convert to string if needed

# Reverse the digits

# If originally float → keep decimal point in reversed position
# Print the list of reversed numbers as strings.


values = [input(f"Enter value {i+1}: ") for i in range(5)]
reversed_list = []

for v in values:
    # Convert to string if number
    try:
        num = float(v)
        str_num = str(num)
        if '.' in str_num:
            integer_part, decimal_part = str_num.split(".")
            reversed_num = integer_part[::-1] + "." + decimal_part[::-1]
        else:
            reversed_num = str_num[::-1]
        reversed_list.append(reversed_num)
    except ValueError:
        reversed_list.append(v[::-1])  # Reverse non-numeric string

print("Reversed numbers/strings:", reversed_list)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
