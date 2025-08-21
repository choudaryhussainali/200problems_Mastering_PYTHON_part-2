# Problem 179
# Find the "mode" value(s) in a dictionary (value that occurs most frequently).
def mode_values(d: dict):
    freq = {}
    for v in d.values():
        freq[v] = freq.get(v, 0) + 1
    max_count = max(freq.values())
    return [val for val, count in freq.items() if count == max_count]

# Example
print(mode_values({"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
