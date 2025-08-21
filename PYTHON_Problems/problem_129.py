# Problem 129
# Generate all possible permutations of a list without using itertools.
def permutations(lst):
    if len(lst)<=1:
        return [lst]
    result = []
    for i in range(len(lst)):
        rest = lst[:i]+lst[i+1:]
        for p in permutations(rest):
            result.append([lst[i]]+p)
    return result

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
