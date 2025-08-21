# Input: A list of numbers → Output: Second largest number
# Example: [3, 7, 1, 9, 5] → Output: 7

## solution 1

a = list(map(int, input("Enter the list numbers using Spaces ; ").split()))
first_max = max(a)
b = a.copy()
b.remove(first_max)
print(f"{max(b)}")

# Solution 2

def second_largest(nums):
    unique_nums = list(set(nums))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[1]

print(second_largest([3, 7, 1, 9, 5]))  # Output: 7


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
