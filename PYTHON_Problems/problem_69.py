# Write a function that returns all unique permutations of a list that may contain duplicates.

# [1, 1, 2]  
# Output: [[1,1,2], [1,2,1], [2,1,1]]


def unique_permutations(nums):
    result = []
    nums.sort()
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            # Skip used numbers
            if used[i]:
                continue
            # Skip duplicates at the same tree level
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue

            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return result


# Test
print(unique_permutations([1, 1, 2]))


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
