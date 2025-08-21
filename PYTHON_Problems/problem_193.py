# Problem 193
# Use a lambda with filter() to extract words that start and end with the same letter.
words = ["level", "apple", "radar", "data", "banana"]
filtered = list(filter(lambda w: w[0] == w[-1], words))
print(filtered)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
