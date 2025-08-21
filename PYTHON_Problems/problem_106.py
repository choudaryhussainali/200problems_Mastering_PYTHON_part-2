# Exercise 26: Numeric Character Replacement

# Take a string input from the user containing digits and letters. Replace:

# Even digits → "X"

# Odd digits → "Y"
# Print the transformed string.

text = input("Enter a string with digits and letters: ")
transformed = ""

for ch in text:
    if ch.isdigit():
        if int(ch) % 2 == 0:
            transformed += "X"
        else:
            transformed += "Y"
    else:
        transformed += ch

print("Transformed string:", transformed)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
