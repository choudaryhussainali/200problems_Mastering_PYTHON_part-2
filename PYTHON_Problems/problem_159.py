# Problem 159
# Find common keys between two dictionaries and return a dictionary with those keys and their values as tuples.

def common_keys(d1: dict, d2: dict):
    return {k: (d1[k], d2[k]) for k in d1 if k in d2}

# Example
print(common_keys({"a": 1, "b": 2}, {"b": 3, "c": 4}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
