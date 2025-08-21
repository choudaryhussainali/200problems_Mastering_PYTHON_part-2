# Input: "Python is fun"
# Output: "nohtyP si nuf"
# (Only reverse each word, not the sentence)


def reverse_words(str):
    reverse = ""
    for word in str.split():
        reverse += word[::-1]+" "

    return reverse

print(reverse_words("Python is fun"))



## SOLUTION 2

def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split())

# Sample Input
print(reverse_words("Python is fun"))

# Output:
# nohtyP si nuf


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
