"""
Title: Anagram Checker
Level: Beginner
Task: Write a function are_anagrams(word1, word2) that returns True if the words are anagrams, False otherwise.
Examples:
    are_anagrams("listen", "silent") -> True
    are_anagrams("hello", "world") -> False
    are_anagrams("triangle", "integral") -> True
    are_anagrams("", "") -> True
"""

def are_anagrams(word1: str, word2: str) -> bool:
    word1_clean = word1.replace(" ", "").lower()
    word2_clean = word2.replace(" ", "").lower()
    return len(word1_clean) == len(word2_clean) and sorted(word1_clean) == sorted(word2_clean)

if __name__ == "__main__":
    print(are_anagrams("listen", "silent"))
    print(are_anagrams("hello", "world"))
    print(are_anagrams("triangle", "integral"))
    print(are_anagrams("", ""))


# ----------------------------------------
# Author: hygroupseries
# GitHub: https://github.com/hygroupseries
# ----------------------------------------    