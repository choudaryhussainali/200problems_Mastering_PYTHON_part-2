# Problem 153
# Count the frequency of each word in a list and return the most frequent word(s).

def most_frequent_word(words: list):
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    max_count = max(freq.values())
    return [w for w, c in freq.items() if c == max_count]

# Example
print(most_frequent_word(["apple", "banana", "apple", "orange", "banana", "apple"]))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
