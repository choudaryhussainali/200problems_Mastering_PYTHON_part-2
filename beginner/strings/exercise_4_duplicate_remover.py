"""
Title: Remove Duplicate Characters
Level: Beginner
Task: Write a function remove_duplicates(text) that returns text with duplicate characters removed while preserving order.
Examples:
    remove_duplicates("hello") -> "helo"
    remove_duplicates("programming") -> "progamin"
    remove_duplicates("mississippi") -> "misp"
    remove_duplicates("") -> ""
"""

def remove_duplicates(text: str) -> str:
    seen = set()
    result = []
    
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)

if __name__ == "__main__":
    print(remove_duplicates("hello"))
    print(remove_duplicates("programming"))
    print(remove_duplicates("mississippi"))
    print(remove_duplicates(""))


# ----------------------------------------
# Author: hygroupseries
# GitHub: https://github.com/hygroupseries
# ----------------------------------------