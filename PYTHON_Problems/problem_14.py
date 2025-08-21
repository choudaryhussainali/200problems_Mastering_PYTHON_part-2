# Input: A string like "Hello 123 world"
# Output:
# Digits: 3
# Alphabets: 10
# Spaces: 2

def count_letters(str):
    Digits = Alphabets = Spaces = 0

    for ch in str:
        if ch.isdigit():
            Digits += 1

        if ch.isalpha():
            Alphabets+=1

        if ch.isspace():
            Spaces +=1

    return Digits, Alphabets, Spaces




s = "Hello 123 world"
d, a, sp = count_letters(s)
print("Digits:", d)
print("Alphabets:", a)
print("Spaces:", sp)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
