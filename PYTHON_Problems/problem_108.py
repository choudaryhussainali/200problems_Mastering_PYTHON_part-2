# Exercise 28: Dynamic Type Multiplier

# Ask the user for 6 inputs (any type). Then:

# Integers → multiply by 3

# Floats → multiply by 1.5

# Strings → repeat twice
# Print the final transformed list.


values = [input(f"Enter value {i+1}: ") for i in range(6)]
transformed = []

for v in values:
    try:
        num = int(v)
        transformed.append(num * 3)
        continue
    except ValueError:
        pass

    try:
        num = float(v)
        transformed.append(num * 1.5)
        continue
    except ValueError:
        pass

    transformed.append(v * 2)  # Repeat strings

print("Transformed list:", transformed)



# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
