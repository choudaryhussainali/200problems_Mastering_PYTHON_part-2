"""
Title: Palindrome Checker
Level: Beginner
Task: Write a function is_palindrome(word) that returns True if word is a palindrome, False otherwise.
Examples:
    is_palindrome("racecar") -> True
    is_palindrome("hello") -> False
    is_palindrome("madam") -> True
    is_palindrome("") -> True
"""

def is_palindrome(word: str) -> bool:
    return word == word[::-1]

if __name__ == "__main__":
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("madam"))
    print(is_palindrome(""))


# ----------------------------------------
# Author: hygroupseries
# GitHub: https://github.com/hygroupseries
# ----------------------------------------