# 1️⃣ String & Character Logic
# Problem:
# Write a function longest_vowel_substring(s) that returns the length of the longest
#  consecutive substring containing only vowels (a, e, i, o, u)

def longest_vowel_substring(s):
    vowels = set("aeiouAEIOU")  # Include uppercase vowels too
    max_length = 0
    current_length = 0

    for char in s:
        if char in vowels:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0  # reset count if consonant found

    return max_length


# Test
print(longest_vowel_substring("helloooaeioubb"))  # Output: 6
print(longest_vowel_substring("abcdeeeiiioouuu"))  # Output: 10


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
