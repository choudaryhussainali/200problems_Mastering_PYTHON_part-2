# 🔹 6. Find Maximum Frequency Element in List
# Write a function to find the number that appears most frequently in a list.

# Sample Input: [2, 3, 2, 5, 2, 3, 5, 5, 5]
# Expected Output: 5


from collections import Counter

def max_frequency_element(lst):
    freq = Counter(lst)
    return max(freq, key=freq.get)

# Sample Input
print(max_frequency_element([2, 3, 2, 5, 2, 3, 5, 5, 5]))

# Output:
# 5


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
