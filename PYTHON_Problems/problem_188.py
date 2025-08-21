# Problem 188
# Use a lambda to find the maximum by custom rule: prioritize even numbers, then value.
nums = [3, 7, 8, 2, 9, 10]
max_val = max(nums, key=lambda x: (x % 2 == 0, x))
print(max_val)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
