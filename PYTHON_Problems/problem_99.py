# Exercise 19: Dynamic List Summation

# Take 7 inputs. Some may be strings, integers, or floats. Create two lists:

# List of all numbers → sum them

# List of all strings → sum their lengths
# Print both sums.

values = [input(f"Enter value {i+1}: ") for i in range(7)]
number_sum = 0
string_length_sum = 0

for v in values:
    try:
        num = int(v)
        number_sum += num
    except ValueError:
        try:
            num = float(v)
            number_sum += num
        except ValueError:
            if isinstance(v, str):
                string_length_sum += len(v)

print("Sum of numbers:", number_sum)
print("Sum of string lengths:", string_length_sum)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
