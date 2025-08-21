# # Example
# my_dict = {"a": 1, "b": 2, "c": 3}
# # Output: {1: 'a', 2: 'b', 3: 'c'}

def swap_keys_values(d):
    return {v: k for k, v in d.items()}

data = {"a": 1, "b": 2, "c": 3}
print(swap_keys_values(data))  # {1: 'a', 2: 'b', 3: 'c'}


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
