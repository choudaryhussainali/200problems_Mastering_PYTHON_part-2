# Problem 160
# Group words by their first letter using a dictionary.

def group_by_first_letter(words: list):
    grouped = {}
    for word in words:
        grouped.setdefault(word[0], []).append(word)
    return grouped

# Example
print(group_by_first_letter(["apple", "ant", "banana", "bat", "cat"]))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
