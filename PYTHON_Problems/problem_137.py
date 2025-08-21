# Problem 137: From a list of words, group them into lists of anagrams.
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        groups[''.join(sorted(word))].append(word)
    return list(groups.values())

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
