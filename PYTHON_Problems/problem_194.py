# Problem 194
# Use reduce() with lambda to find the greatest common divisor (GCD) of a list of numbers.
from functools import reduce
import math
nums = [48, 64, 80]
gcd = reduce(lambda a, b: math.gcd(a, b), nums)
print(gcd)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
