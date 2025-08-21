# Input: "banana"
# Output: {'b': 1, 'a': 3, 'n': 2}



a= str(input("Enter Your WORD :"))
frquency = {}

for i in a:
    if i in frquency.keys():
        frquency[i] += 1

    else:
        frquency[i] = 1

print(frquency)

## Solution 2

def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

print(char_frequency("banana"))  # Output: {'b': 1, 'a': 3, 'n': 2}


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
