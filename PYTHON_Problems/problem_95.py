# Exercise 15: Mixed Type Sort & Filter

# Take 8 inputs from the user (strings, integers, or floats). Then:

# Create a list of all numbers greater than 10.

# Create a list of all strings longer than 3 characters.

# Print both lists.

values = [input(f"Enter value {i+1}: ") for i in range(8)]
numbers_above_10 = []
strings_longer_3 = []

for v in values:
    try:
        num = int(v)
        if num > 10:
            numbers_above_10.append(num)
    except ValueError:
        try:
            num = float(v)
            if num > 10:
                numbers_above_10.append(num)
        except ValueError:
            # Treat as string
            if len(v) > 3:
                strings_longer_3.append(v)

print("Numbers greater than 10:", numbers_above_10)
print("Strings longer than 3 chars:", strings_longer_3)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
