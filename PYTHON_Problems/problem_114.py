# Problem 114: Find the majority element in a list (the element that appears more than n/2 times).
# Example: [3,3,4,2,3,3,5,3] → 3

def majority_element(nums):
    count, candidate = 0, None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

print(majority_element([3,3,4,2,3,3,5,3]))
# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
