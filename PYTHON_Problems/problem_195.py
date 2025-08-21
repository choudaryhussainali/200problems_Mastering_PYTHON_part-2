# Problem 195
# Use a lambda to sort strings by the number of vowels they contain.
words = ["banana", "pear", "grape", "blueberry"]
vowel_count = lambda s: sum(1 for ch in s if ch in "aeiou")
sorted_words = sorted(words, key=vowel_count, reverse=True)
print(sorted_words)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
