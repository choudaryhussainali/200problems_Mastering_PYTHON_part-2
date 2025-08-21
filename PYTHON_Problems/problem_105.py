# Exercise 25: Mixed Type Filter

# Take 8 inputs from the user. Separate them into three lists:

# Integers greater than 10

# Floats less than 10

# Strings with length ≥ 3
# Print all three lists.

values = [input(f"Enter value {i+1}: ") for i in range(8)]
integers_gt_10 = []
floats_lt_10 = []
strings_len3 = []

for v in values:
    try:
        num = int(v)
        if num > 10:
            integers_gt_10.append(num)
    except ValueError:
        try:
            num = float(v)
            if num < 10:
                floats_lt_10.append(num)
        except ValueError:
            if len(v) >= 3:
                strings_len3.append(v)

print("Integers > 10:", integers_gt_10)
print("Floats < 10:", floats_lt_10)
print("Strings length >= 3:", strings_len3)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
