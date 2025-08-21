# Exercise 7: Smart Average Calculator

# Take 5 inputs from the user. Some may be integers, floats, or numeric strings. Some could be invalid (like "abc").

# Convert only valid numeric inputs.

# Calculate the average of the valid numbers.

# Print how many inputs were invalid.

total = 0
count = 0
invalid = 0

for i in range(5):
    value = input(f"Enter value {i+1}: ")
    try:
        num = int(value)
    except ValueError:
        try:
            num = float(value)
        except ValueError:
            invalid += 1
            continue
    total += num
    count += 1

if count > 0:
    average = total / count
    print("Average of valid numbers:", average)
else:
    print("No valid numbers entered.")

print("Invalid inputs:", invalid)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
