# Problem 168
# Merge a list of dictionaries into one, summing values of duplicate keys.
def merge_sum_dicts(dicts: list):
    result = {}
    for d in dicts:
        for k, v in d.items():
            result[k] = result.get(k, 0) + v
    return result

# Example
print(merge_sum_dicts([{"a": 1, "b": 2}, {"a": 3, "c": 4}, {"b": 5}]))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
