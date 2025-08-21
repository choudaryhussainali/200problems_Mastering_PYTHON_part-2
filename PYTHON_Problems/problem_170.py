# Problem 170
# Given a dictionary of strings, replace all vowels in keys with "*" and return the new dict.
def mask_vowels_in_keys(d: dict):
    vowels = "aeiouAEIOU"
    def mask(word): return ''.join('*' if ch in vowels else ch for ch in word)
    return {mask(k): v for k, v in d.items()}

# Example
print(mask_vowels_in_keys({"apple": 1, "banana": 2, "grape": 3}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
