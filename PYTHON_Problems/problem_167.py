# Problem 167
# Given a nested dictionary, count how many total keys it contains (including nested ones).
def count_keys(d: dict):
    count = 0
    for v in d.values():
        if isinstance(v, dict):
            count += count_keys(v)
    return count + len(d)

# Example
print(count_keys({"a": {"b": {"c": 1}}, "d": 2}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
