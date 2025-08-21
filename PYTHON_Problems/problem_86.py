# Exercise 6: Numeric Palindrome Checker

# Ask the user to enter a number (integer or float). Convert it appropriately and check
#  if it is a palindrome (reads the same forwards and backwards). Ignore the decimal point for floats.

value = input("Enter a number: ")

# Convert to float or int
try:
    num = int(value)
    str_num = str(num)
except ValueError:
    try:
        num = float(value)
        str_num = str(num).replace(".", "")  # Ignore decimal point
    except ValueError:
        print("Invalid input! Please enter a number.")
        str_num = None

if str_num:
    if str_num == str_num[::-1]:
        print(f"{value} is a palindrome.")
    else:
        print(f"{value} is not a palindrome.")


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
