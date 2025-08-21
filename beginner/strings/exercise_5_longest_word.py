"""
Title: Find Longest Word
Level: Beginner
Task: Write a function find_longest_word(sentence) that returns the longest word in the sentence.
Examples:
    find_longest_word("The quick brown fox jumps") -> "quick"
    find_longest_word("Python programming is fun") -> "programming"
    find_longest_word("Hello world") -> "Hello"
    find_longest_word("") -> ""
"""

def find_longest_word(sentence: str) -> str:
    words = sentence.split()
    if not words:
        return ""
    
    return max(words, key=len)

if __name__ == "__main__":
    print(find_longest_word("The quick brown fox jumps"))
    print(find_longest_word("Python programming is fun"))
    print(find_longest_word("Hello world"))
    print(find_longest_word(""))


# ----------------------------------------
# Author: hygroupseries
# GitHub: https://github.com/hygroupseries
# ----------------------------------------