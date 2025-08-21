# Problem 175
# Given dict of word->frequency, return the most common word(s).
def most_common_words(freq: dict):
    if not freq:
        return []
    max_val = max(freq.values())
    return [w for w, f in freq.items() if f == max_val]

# Example
print(most_common_words({"apple": 5, "banana": 3, "orange": 5}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
