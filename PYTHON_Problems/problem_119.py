# Problem 119: Find the kth largest element in a list without sorting the entire list.
# Example: [3,2,1,5,6,4], k=2 → 5

import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

print(kth_largest([3,2,1,5,6,4], 2))
# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
