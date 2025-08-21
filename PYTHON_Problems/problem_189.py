# Problem 189
# Use a lambda with filter() to remove None and empty strings from a list.
items = ["apple", "", None, "banana", " ", "kiwi"]
cleaned = list(filter(lambda x: x and x.strip(), items))
print(cleaned)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
