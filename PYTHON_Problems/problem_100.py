# Exercise 20: Mixed Input Transformer

# Take 5 inputs from the user (any type). Then:

# If integer → multiply by 5

# If float → divide by 2

# If string → repeat it 3 times
# Print the transformed list.


values = [input(f"Enter value {i+1}: ") for i in range(5)]
transformed_list = []

for v in values:
    # Try int
    try:
        num = int(v)
        transformed_list.append(num * 5)
        continue
    except ValueError:
        pass

    # Try float
    try:
        num = float(v)
        transformed_list.append(num / 2)
        continue
    except ValueError:
        pass

    # Treat as string
    transformed_list.append(v * 3)

print("Transformed list:", transformed_list)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
