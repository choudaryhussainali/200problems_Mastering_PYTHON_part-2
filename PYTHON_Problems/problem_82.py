# Exercise 2: Swap Without Temporary Variable

# Take two inputs from the user. They could be integers or floats. Swap their values without using a third variable.
# Goal: Logical reasoning + understanding of arithmetic operations.

a = input("Enter first number: ")
b = input("Enter second number: ")

# Convert to float or int
a = float(a) if '.' in a else int(a)
b = float(b) if '.' in b else int(b)

# Swap without temp
a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, ", b =", b)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
