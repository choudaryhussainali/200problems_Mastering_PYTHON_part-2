# Problem 200
# Use a lambda to transform a list of numbers into dict {n: "even"/"odd"}.
nums = [1, 2, 3, 4, 5, 6]
parity = dict(map(lambda x: (x, "even" if x % 2 == 0 else "odd"), nums))
print(parity)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
