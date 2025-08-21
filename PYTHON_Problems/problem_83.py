# Exercise 3: Reverse Input Types

# Ask the user to input a value.

# If it’s an integer, convert it to a string and reverse the digits.

# If it’s a float, convert it to a string and reverse the digits before and after the decimal separately.

# If it’s a string, try to convert it to int or float if possible, otherwise keep it as a string and print its ASCII codes.
# Goal: Advanced type conversion + string manipulation + logical thinking.

value = input("Enter a value: ")

# Try integer
try:
    num = int(value)
    reversed_num = int(str(num)[::-1])
    print("Reversed integer:", reversed_num)
except ValueError:
    # Try float
    try:
        num = float(value)
        integer_part, decimal_part = str(num).split(".")
        reversed_float = float(integer_part[::-1] + "." + decimal_part[::-1])
        print("Reversed float:", reversed_float)
    except ValueError:
        # It's a string
        try:
            num = float(value)
            print("Converted to float:", num)
        except ValueError:
            ascii_codes = [ord(ch) for ch in value]
            print("ASCII codes:", ascii_codes)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
