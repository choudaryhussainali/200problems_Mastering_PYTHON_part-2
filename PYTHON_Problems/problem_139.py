# Problem 139: Rearrange a list so that even-indexed elements are greater than their neighbors (wiggle sort).
def wiggle_sort(nums):
    nums.sort()
    half = (len(nums)+1)//2
    left, right = nums[:half][::-1], nums[half:][::-1]
    nums[:] = [val for pair in zip(left, right) for val in pair]
    if len(left) > len(right):
        nums.append(left[-1])

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
