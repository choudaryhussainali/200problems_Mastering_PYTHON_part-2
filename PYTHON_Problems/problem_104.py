# Exercise 24: Type-Based Conditional Transformation

# Ask the user to enter 4 values of any type. Then:

# Integers → cube

# Floats → round to nearest integer

# Strings → reverse

# Other → replace with "N/A"
# Print the transformed list.

values = [input(f"Enter value {i+1}: ") for i in range(4)]
transformed = []

for v in values:
    try:
        num = int(v)
        transformed.append(num ** 3)
        continue
    except ValueError:
        pass

    try:
        num = float(v)
        transformed.append(round(num))
        continue
    except ValueError:
        pass

    if isinstance(v, str):
        transformed.append(v[::-1])
    else:
        transformed.append("N/A")

print("Transformed list:", transformed)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
