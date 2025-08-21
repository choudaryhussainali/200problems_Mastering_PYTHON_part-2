# Problem 173
# Flatten a dictionary with tuple keys created from nested keys.
def flatten_dict(d: dict, parent_key=()):
    items = {}
    for k, v in d.items():
        new_key = parent_key + (k,)
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key))
        else:
            items[new_key] = v
    return items

# Example
print(flatten_dict({"a": {"b": {"c": 1}}, "d": 2}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
