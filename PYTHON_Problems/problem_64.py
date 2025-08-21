# 4️⃣ Subarray Sum Divisible by K
# count_subarrays_divisible_by_k([4,5,0,-2,-3,1], 5)  # Output: 7


def count_subarrays_divisible_by_k(nums, k):
    count = 0
    prefix_sum = 0
    remainder_freq = {0: 1}  # remainder: frequency

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k
        
        # Handle negative remainders
        if remainder < 0:
            remainder += k

        if remainder in remainder_freq:
            count += remainder_freq[remainder]
        
        remainder_freq[remainder] = remainder_freq.get(remainder, 0) + 1

    return count


# Test
print(count_subarrays_divisible_by_k([4, 5, 0, -2, -3, 1], 5))  # Output: 7


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
