# Problem 158
# Sort a dictionary by its values in descending order.

def sort_dict_by_values(d: dict):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

# Example
print(sort_dict_by_values({"a": 3, "b": 1, "c": 2}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
