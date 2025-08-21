
# 🔹 5. Check if List is Sorted
# Create a function that returns True if the list is sorted in ascending order.

# Sample Input: [1, 2, 3, 4]
# Expected Output: True

# Sample Input: [1, 4, 3]
# Expected Output: False

def is_sorted(lst):
    return lst == sorted(lst)

# Sample Input
print(is_sorted([1, 2, 3, 4]))   # True
print(is_sorted([1, 4, 3]))      # False


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
