# Problem 111: Find all pairs of numbers in a list whose sum is equal to a target value.
# Example: [2,4,3,5,7,8,1], target=8 → pairs: (3,5), (7,1)

def find_pairs(nums, target):
    pairs = []
    seen = set()
    for num in nums:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
    return pairs

print(find_pairs([2,4,3,5,7,8,1], 8))
# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
