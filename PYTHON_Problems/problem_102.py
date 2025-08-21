# Exercise 22: Sum of Digits for Numbers and Strings

# Take 5 inputs (int, float, or string of digits).

# For numbers → sum all digits ignoring decimal point.

# For strings → sum numeric characters; ignore letters.
# Print a list of digit sums.

values = [input(f"Enter value {i+1}: ") for i in range(5)]
digit_sums = []

for v in values:
    sum_digits = 0
    # Remove non-digit characters
    for ch in v:
        if ch.isdigit():
            sum_digits += int(ch)
    digit_sums.append(sum_digits)

print("Sum of digits for each input:", digit_sums)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
