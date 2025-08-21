# Step 1: Create a file 'sample.txt' with some lines of text
# Step 2: Write a program to count total number of words in that file

# Hint: Use open(), read(), split()



# File creation (if not already made)
with open("sample.txt", "w") as f:
    f.write("Python is powerful.\nYou are learning fast.")

# Word count program
def count_words(filename):
    with open(filename, "r") as f:
        text = f.read()
        words = text.split()
        return len(words)

# Sample Run
print(count_words("sample.txt"))

# Output:
# 7


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
