# Exercise 29: Mixed Input Counter

# Take 8 inputs (any type). Count and print:

# Number of integers

# Number of floats

# Number of strings

# Number of unsupported types


values = [input(f"Enter value {i+1}: ") for i in range(8)]
int_count = 0
float_count = 0
str_count = 0
other_count = 0

for v in values:
    try:
        int(v)
        int_count += 1
    except ValueError:
        try:
            float(v)
            float_count += 1
        except ValueError:
            if isinstance(v, str):
                str_count += 1
            else:
                other_count += 1

print("Integers:", int_count)
print("Floats:", float_count)
print("Strings:", str_count)
print("Other types:", other_count)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
