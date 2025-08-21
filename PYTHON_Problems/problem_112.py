# Problem 112: Given a list of integers, find the longest increasing subsequence (not necessarily contiguous).
# Example: [10,9,2,5,3,7,101,18] → [2,3,7,101]

def longest_increasing_subsequence(nums):
    from bisect import bisect_left
    sub = []
    for x in nums:
        i = bisect_left(sub, x)
        if i == len(sub):
            sub.append(x)
        else:
            sub[i] = x
    return sub

print(longest_increasing_subsequence([10,9,2,5,3,7,101,18]))
# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
