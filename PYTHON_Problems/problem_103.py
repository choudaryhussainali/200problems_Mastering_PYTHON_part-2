# Exercise 23: Swap and Convert

# Ask the user to input two values (int, float, or numeric strings).

# Swap them.

# Convert the first to float, the second to int.
# Print the new values and their types.

a = input("Enter first value: ")
b = input("Enter second value: ")

# Swap
a, b = b, a

# Convert
try:
    a = float(a)
except ValueError:
    print(f"Cannot convert '{a}' to float")

try:
    b = int(float(b))  # Convert numeric strings to int
except ValueError:
    print(f"Cannot convert '{b}' to int")

print("After swap and conversion:")
print("First value:", a, "Type:", type(a))
print("Second value:", b, "Type:", type(b))


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
