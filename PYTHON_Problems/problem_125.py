# Problem 125
# Partition a list into all possible sublists of consecutive elements.
def consecutive_sublists(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            result.append(lst[i:j])
    return result

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
