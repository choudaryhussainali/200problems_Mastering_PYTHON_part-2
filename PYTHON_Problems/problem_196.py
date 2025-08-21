# Problem 196
# Use a lambda with map() to flatten a 2D list into a 1D list.
matrix = [[1,2],[3,4],[5,6]]
flattened = list(map(lambda pair: pair[0] + pair[1], [[i, 0] if isinstance(i, int) else i for sub in matrix for i in sub]))
print(flattened)
# Note: demonstrates trickiness of map+lambda flatten

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
