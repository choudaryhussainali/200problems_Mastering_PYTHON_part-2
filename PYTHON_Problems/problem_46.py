# Create a file 'text.txt' with some paragraphs.

# Task:
# Write a function to return:
# - Total lines
# - Total words
# - Total characters

# Output:
# Lines: 5 | Words: 53 | Characters: 278

def file_stats(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
    print("Lines:", len(lines))
    print("Words:", word_count)
    print("Characters:", char_count)

file_stats("text.txt")

# Lines: 5 | Words: 53 | Characters: 278


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
