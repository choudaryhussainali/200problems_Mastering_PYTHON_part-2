# Exercise 16: Alternating Type List

# Ask the user to input 6 values. Convert numeric strings to numbers. Then create a new list where:

# Even-indexed elements are converted to strings

# Odd-indexed elements are converted to numbers (int if possible, else float)

values = [input(f"Enter value {i+1}: ") for i in range(6)]
new_list = []

for i, v in enumerate(values):
    # Convert to number if possible
    try:
        num = int(v)
    except ValueError:
        try:
            num = float(v)
        except ValueError:
            num = v  # Keep as string

    # Apply alternating conversion
    if i % 2 == 0:
        new_list.append(str(num))
    else:
        if isinstance(num, str):
            # Try converting string to int or float
            try:
                num = int(num)
            except ValueError:
                try:
                    num = float(num)
                except ValueError:
                    pass
        new_list.append(num)

print("Transformed list:", new_list)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
