# Task:
# Write a calculator that divides two numbers.
# If denominator is zero, print: "Cannot divide by zero!"

# Input: a = 10, b = 0
# Output: Cannot divide by zero!

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"

print(divide(10, 0))



# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
