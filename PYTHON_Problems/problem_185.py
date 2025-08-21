# Problem 185
# Use a lambda with sorted() to sort strings by length, then alphabetically.
words = ["apple", "pear", "banana", "kiwi", "grape"]
sorted_words = sorted(words, key=lambda x: (len(x), x))
print(sorted_words)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
