"""
Title: Vowel and Consonant Counter
Level: Beginner
Task: Write a function count_vowels_consonants(text) that returns a tuple (vowel_count, consonant_count).
Examples:
    count_vowels_consonants("Hello World") -> (3, 7)
    count_vowels_consonants("Python Programming") -> (4, 11)
    count_vowels_consonants("A E I O U") -> (5, 0)
    count_vowels_consonants("") -> (0, 0)
"""

def count_vowels_consonants(text: str) -> tuple:
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return (vowel_count, consonant_count)

if __name__ == "__main__":
    print(count_vowels_consonants("Hello World"))
    print(count_vowels_consonants("Python Programming"))
    print(count_vowels_consonants("A E I O U"))
    print(count_vowels_consonants("b c d f g"))
    print(count_vowels_consonants(""))


# ----------------------------------------
# Author: hygroupseries
# GitHub: https://github.com/hygroupseries
# ----------------------------------------