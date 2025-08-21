# Problem 116: Find the subarray with the maximum sum (Kadane’s Algorithm).
# Example: [-2,1,-3,4,-1,2,1,-5,4] → 6 ([4,-1,2,1])

def max_subarray(nums):
    max_sum = cur_sum = nums[0]
    for num in nums[1:]:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)
    return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
