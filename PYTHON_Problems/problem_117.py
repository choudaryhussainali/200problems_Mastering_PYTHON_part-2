# Problem 117: Flatten a deeply nested list without using recursion.
# Example: [1,[2,[3,4],5],6] → [1,2,3,4,5,6]

def flatten_list(nested):
    result, stack = [], nested[::-1]
    while stack:
        cur = stack.pop()
        if isinstance(cur, list):
            stack.extend(cur[::-1])
        else:
            result.append(cur)
    return result

print(flatten_list([1,[2,[3,4],5],6]))
# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
