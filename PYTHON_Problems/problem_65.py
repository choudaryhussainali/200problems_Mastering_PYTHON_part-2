# 5️⃣ Custom Sorting with Multiple Rules
# Problem:
# Given a list of words, sort them:

# By length (shorter first)

# If lengths are equal, sort alphabetically.

def custom_sort(words):
    # Sort by length first, then alphabetically if lengths are same
    return sorted(words, key=lambda x: (len(x), x.lower()))


# Test
words = ["apple", "kiwi", "banana", "fig", "grape", "pear", "apricot"]
print(custom_sort(words))


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
