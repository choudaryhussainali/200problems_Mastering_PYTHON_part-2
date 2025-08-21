# Problem 133: Partition a list into k sublists such that the largest sum of any sublist is minimized.
def can_partition(nums, k, max_sum):
    cnt, cur = 1, 0
    for num in nums:
        if cur + num > max_sum:
            cnt += 1
            cur = num
            if cnt > k:
                return False
        else:
            cur += num
    return True

def split_array(nums, k):
    l, r = max(nums), sum(nums)
    while l < r:
        mid = (l+r)//2
        if can_partition(nums, k, mid):
            r = mid
        else:
            l = mid+1
    return l

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
