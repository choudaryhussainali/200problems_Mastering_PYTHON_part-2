# Exercise 12: Type Mixer Game

# Ask the user to enter 5 values of any type. Convert numeric strings to numbers. Then:

# Replace integers with their square.

# Replace floats with their half.

# Replace strings with their length.
# Print the new list.


values = [input(f"Enter value {i+1}: ") for i in range(5)]
new_list = []

for v in values:
    # Try int first
    try:
        num = int(v)
        new_list.append(num ** 2)
        continue
    except ValueError:
        pass

    # Try float
    try:
        num = float(v)
        new_list.append(num / 2)
        continue
    except ValueError:
        pass

    # Treat as string
    new_list.append(len(v))

print("Transformed list:", new_list)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
