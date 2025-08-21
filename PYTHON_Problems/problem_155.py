# Problem 155
# Given a nested dictionary, flatten it so that nested keys are joined with ".".

def flatten_dict(d: dict, parent_key="", sep="."):
    items = {}
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
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
