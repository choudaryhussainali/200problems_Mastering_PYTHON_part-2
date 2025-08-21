# Problem 164
# Find the symmetric difference between two dictionaries' keys.
def dict_symmetric_difference(d1: dict, d2: dict):
    return (set(d1.keys()) ^ set(d2.keys()))

# Example
print(dict_symmetric_difference({"a": 1, "b": 2}, {"b": 3, "c": 4}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
