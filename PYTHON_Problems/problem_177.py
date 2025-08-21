# Problem 177
# Invert a dictionary of lists: element -> list of keys containing it.
def invert_dict_of_lists(d: dict):
    inverted = {}
    for k, values in d.items():
        for v in values:
            inverted.setdefault(v, []).append(k)
    return inverted

# Example
print(invert_dict_of_lists({"a": [1, 2], "b": [2, 3], "c": [3, 1]}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
