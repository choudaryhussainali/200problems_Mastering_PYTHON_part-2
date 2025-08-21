# Problem 197
# Use a lambda with sorted() to order tuples first by absolute value of first element, then by second element.
pairs = [(-3, 2), (3, 1), (-2, 5), (2, 4)]
sorted_pairs = sorted(pairs, key=lambda x: (abs(x[0]), x[1]))
print(sorted_pairs)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
