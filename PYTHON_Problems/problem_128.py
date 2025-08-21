# Problem 128
# Given a list, split into k nearly equal-sized parts.
def split_list(lst, k):
    n = len(lst)
    avg, rem = divmod(n, k)
    parts = []
    start = 0
    for i in range(k):
        end = start + avg + (1 if i<rem else 0)
        parts.append(lst[start:end])
        start = end
    return parts

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
