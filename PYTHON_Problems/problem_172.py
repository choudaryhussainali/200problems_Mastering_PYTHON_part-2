# Problem 172
# Check if a dictionary is "balanced": all values have the same data type.
def is_balanced_dict(d: dict):
    types = {type(v) for v in d.values()}
    return len(types) == 1

# Example
print(is_balanced_dict({"a": 1, "b": 2, "c": 3}))
print(is_balanced_dict({"a": 1, "b": "x"}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
