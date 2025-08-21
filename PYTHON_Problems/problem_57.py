# # Example
# number = 12345
# # Output: 15


def sum_of_digits(num):
    return sum(int(digit) for digit in str(abs(num)))

number = 12345
print(sum_of_digits(number))  # 15


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
