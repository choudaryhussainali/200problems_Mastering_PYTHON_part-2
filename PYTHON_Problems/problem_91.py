# Exercise 11: Character Code Manipulation

# Ask the user to enter a string. Convert each character to its ASCII code, then:

# If the code is even, divide by 2.

# If the code is odd, multiply by 3 and add 1.
# Print the final list of numbers.

text = input("Enter a string: ")
result = []

for ch in text:
    code = ord(ch)
    if code % 2 == 0:
        result.append(code // 2)
    else:
        result.append(code * 3 + 1)

print("Transformed codes:", result)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
