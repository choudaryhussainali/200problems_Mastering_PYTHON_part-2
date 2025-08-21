# Exercise 13: Smart Type Summation

# Ask the user to enter 10 values. Some may be strings, integers, or floats. Sum all numbers, and concatenate all strings. Ignore unsupported types.

values = [input(f"Enter value {i+1}: ") for i in range(10)]
sum_numbers = 0
concat_strings = ""

for v in values:
    try:
        num = int(v)
        sum_numbers += num
    except ValueError:
        try:
            num = float(v)
            sum_numbers += num
        except ValueError:
            if isinstance(v, str):
                concat_strings += v

print("Sum of numbers:", sum_numbers)
print("Concatenated strings:", concat_strings)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
