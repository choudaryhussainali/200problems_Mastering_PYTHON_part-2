# Problem 136: Rotate a list in-place to the right by k steps without using extra space.
def rotate(nums, k):
    n = len(nums)
    k %= n
    nums[:] = nums[-k:] + nums[:-k]

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
