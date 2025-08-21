# Exercise 9: Mixed Data Sorter

# Ask the user to enter 10 values (integers, floats, or numeric strings). Convert all to numbers.

# Separate them into integers and floats.

# Sort integers in ascending order.

# Sort floats in descending order.

# Print both lists.

values = [input(f"Enter value {i+1}: ") for i in range(10)]

integers = []
floats = []

for v in values:
    try:
        num = int(v)
        integers.append(num)
    except ValueError:
        try:
            num = float(v)
            floats.append(num)
        except ValueError:
            continue  # Ignore invalid inputs

integers.sort()
floats.sort(reverse=True)

print("Sorted integers (asc):", integers)
print("Sorted floats (desc):", floats)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
