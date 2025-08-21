# 🔹 9. Capitalize First Letter of Each Word
# Write a function to capitalize the first letter of each word in a sentence.

# Sample Input: "python is powerful"
# Expected Output: "Python Is Powerful"

def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

# Sample Input
print(capitalize_words("python is powerful"))

# Output:
# Python Is Powerful


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
