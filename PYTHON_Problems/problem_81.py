# Exercise 1: Sum of Mixed Data

# Write a program that asks the user to enter 5 values, which can be integers, floats, or numeric strings (like "12"). Convert them appropriately and calculate the total sum.
# Goal: Practice type conversion and handling mixed input.

total = 0
for i in range(5):
    value = input(f"Enter value {i+1}: ")
    # Try to convert to int first, then float
    try:
        num = int(value)
    except ValueError:
        try:
            num = float(value)
        except ValueError:
            print(f"'{value}' is not a number. Ignored.")
            continue
    total += num

print("Total sum:", total)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
