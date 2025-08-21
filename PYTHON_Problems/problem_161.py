# Problem 161
# Check if two dictionaries are deeply equal (including nested dictionaries).
def deep_equal(d1: dict, d2: dict) -> bool:
    if d1.keys() != d2.keys():
        return False
    for k in d1:
        v1, v2 = d1[k], d2[k]
        if isinstance(v1, dict) and isinstance(v2, dict):
            if not deep_equal(v1, v2):
                return False
        elif v1 != v2:
            return False
    return True

# Example
print(deep_equal({"a": {"b": 1}}, {"a": {"b": 1}}))
print(deep_equal({"a": {"b": 2}}, {"a": {"b": 1}}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
