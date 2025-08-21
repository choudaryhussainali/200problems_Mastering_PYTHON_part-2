# Problem 132: Given a list of lists, flatten it but keep the unique order of first appearance.
def flatten_unique(lst):
    seen = set()
    result = []
    for sub in lst:
        for x in sub:
            if x not in seen:
                seen.add(x)
                result.append(x)
    return result

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
