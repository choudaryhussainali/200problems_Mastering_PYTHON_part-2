# Problem 178
# Merge two nested dictionaries recursively (deep merge).
def deep_merge(d1: dict, d2: dict):
    result = dict(d1)
    for k, v in d2.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = v
    return result

# Example
print(deep_merge({"a": {"x": 1}, "b": 2}, {"a": {"y": 2}, "c": 3}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
