# Problem 174
# Rotate keys and values in dictionary: if duplicate values, keep only last key.
def rotate_dict(d: dict):
    return {v: k for k, v in d.items()}

# Example
print(rotate_dict({"a": 1, "b": 2, "c": 1}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
