# Problem 152
# Merge two dictionaries but if a key exists in both, store their values in a list instead of overwriting.

def merge_dicts(d1: dict, d2: dict):
    merged = {}
    for k in set(d1) | set(d2):
        if k in d1 and k in d2:
            merged[k] = [d1[k], d2[k]]
        else:
            merged[k] = d1.get(k, d2.get(k))
    return merged

# Example
print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
