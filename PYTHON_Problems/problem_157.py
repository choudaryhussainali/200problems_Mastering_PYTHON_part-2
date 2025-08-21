# Problem 157
# Remove all keys from a dictionary where the value is None or empty string.

def clean_dict(d: dict):
    return {k: v for k, v in d.items() if v not in (None, "")}

# Example
print(clean_dict({"a": 1, "b": None, "c": "", "d": 5}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
