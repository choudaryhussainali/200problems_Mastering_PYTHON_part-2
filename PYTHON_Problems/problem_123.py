# Problem 123
# Given a list of integers, return all unique triplets [a,b,c] such that a+b+c=0.
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l,r = i+1, len(nums)-1
        while l<r:
            s = nums[i]+nums[l]+nums[r]
            if s<0:
                l+=1
            elif s>0:
                r-=1
            else:
                result.append([nums[i], nums[l], nums[r]])
                while l<r and nums[l]==nums[l+1]: l+=1
                while l<r and nums[r]==nums[r-1]: r-=1
                l+=1; r-=1
    return result

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
