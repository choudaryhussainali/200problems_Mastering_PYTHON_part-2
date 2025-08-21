# Problem 156
# Find the key with the maximum value in a dictionary.

def key_with_max_value(d: dict):
    return max(d, key=d.get)

# Example
print(key_with_max_value({"Ali": 90, "Sara": 85, "John": 95}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
