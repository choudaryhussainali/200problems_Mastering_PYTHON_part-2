# Problem 184
# Use reduce() with a lambda to compute factorial of n.
from functools import reduce
n = 6
factorial = reduce(lambda a, b: a * b, range(1, n + 1))
print(factorial)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
