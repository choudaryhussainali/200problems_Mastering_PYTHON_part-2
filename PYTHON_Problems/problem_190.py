# Problem 190
# Use a lambda to count frequency of each element in a list (using dict + setdefault).
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
freq = {}
list(map(lambda x: freq.setdefault(x, 0) or freq.__setitem__(x, freq[x] + 1), nums))
print(freq)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
