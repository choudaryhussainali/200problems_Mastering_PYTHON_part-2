# Problem 154
# Invert a dictionary (swap keys and values). If multiple keys have same value, group them in a list.

def invert_dict(d: dict):
    inverted = {}
    for k, v in d.items():
        inverted.setdefault(v, []).append(k)
    return inverted

# Example
print(invert_dict({"a": 1, "b": 2, "c": 1}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
