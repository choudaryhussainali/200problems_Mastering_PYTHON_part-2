# Problem 199
# Use a lambda to find the second largest unique number in a list.
nums = [10, 20, 30, 20, 40, 40, 50]
second_largest = sorted(set(nums), key=lambda x: -x)[1]
print(second_largest)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
