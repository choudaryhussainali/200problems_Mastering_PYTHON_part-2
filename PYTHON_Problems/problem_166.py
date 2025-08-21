# Problem 166
# Flip a dictionary so that values map to lists of keys, then return only those with more than 1 key.
def find_duplicates(d: dict):
    inverted = {}
    for k, v in d.items():
        inverted.setdefault(v, []).append(k)
    return {v: ks for v, ks in inverted.items() if len(ks) > 1}

# Example
print(find_duplicates({"a": 1, "b": 2, "c": 1, "d": 2, "e": 3}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
