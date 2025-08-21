# Exercise 4: Type Detection and Operations

# Ask the user to enter three values. For each value:

# Print its type.

# If it’s a number (int/float), multiply by 2.

# If it’s a string, reverse it.

# If it’s anything else, print "Unsupported type".
# Goal: Logical branching + type checking + basic operations.

values = [input(f"Enter value {i+1}: ") for i in range(3)]

for v in values:
    # Check for int or float
    try:
        num = int(v)
        print(f"{v} is int, multiplied by 2: {num*2}")
    except ValueError:
        try:
            num = float(v)
            print(f"{v} is float, multiplied by 2: {num*2}")
        except ValueError:
            if isinstance(v, str):
                print(f"{v} is string, reversed: {v[::-1]}")
            else:
                print(f"{v} is Unsupported type")


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
