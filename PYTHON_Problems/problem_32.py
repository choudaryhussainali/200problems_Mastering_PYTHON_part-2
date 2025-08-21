#Sum of digits

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

# Sample Input
print(sum_digits(1234))

# Output:
# 10


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
