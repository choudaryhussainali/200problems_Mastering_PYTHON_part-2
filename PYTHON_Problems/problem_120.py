# Problem 120: Rearrange a list so that positive and negative numbers alternate, maintaining relative order if possible.
# Example: [1,2,3,-4,-1,4] → [1,-4,2,-1,3,4]

def rearrange_alternate(nums):
    pos = [x for x in nums if x >= 0]
    neg = [x for x in nums if x < 0]
    result = []
    while pos or neg:
        if pos: result.append(pos.pop(0))
        if neg: result.append(neg.pop(0))
    return result

print(rearrange_alternate([1,2,3,-4,-1,4]))
# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
