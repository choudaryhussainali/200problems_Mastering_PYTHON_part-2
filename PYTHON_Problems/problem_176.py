# Problem 176
# Detect cycles in a dictionary mapping key->next_key.
def has_cycle(mapping: dict):
    visited = set()
    for start in mapping:
        seen = set()
        cur = start
        while cur in mapping:
            if cur in seen:
                return True
            seen.add(cur)
            cur = mapping[cur]
    return False

# Example
print(has_cycle({"a": "b", "b": "c", "c": "a"}))
print(has_cycle({"a": "b", "b": "c"}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
