# 🔹 10. Sum of Digits Until Single Digit
# Keep summing the digits of a number until the result is a single digit.

# Sample Input: 987 → 9 + 8 + 7 = 24 → 2 + 4 = 6
# Expected Output: 6

def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Sample Input
print(digital_root(987))

# Output:
# 6


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
