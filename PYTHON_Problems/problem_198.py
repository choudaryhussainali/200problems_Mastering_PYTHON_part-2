# Problem 198
# Use a lambda to group words by their first letter (produce dict).
words = ["apple", "ant", "banana", "berry", "carrot"]
grouped = {}
list(map(lambda w: grouped.setdefault(w[0], []).append(w), words))
print(grouped)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
