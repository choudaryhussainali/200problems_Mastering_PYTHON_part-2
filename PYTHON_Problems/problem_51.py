# 1. Dictionary Merge and Sort
# Write a program that merges two dictionaries and then sorts them by keys.

dict1 = {"b": 2, "a": 1}
dict2 = {"d": 4, "c": 3}

# # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

dict3 = {**dict1, **dict2}
sorted_dict = dict(sorted(dict3.items()))
print(sorted_dict)


# solution 2



# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
