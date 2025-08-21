# Implement a function that returns the running median after each new number is added from a stream.
#Input: [2, 1, 5, 7, 2, 0, 5]  
#Output: [2, 1.5, 2, 3.5, 2, 2.0, 2]


import bisect

def running_median(stream):
    sorted_list = []
    medians = []

    for num in stream:
        # Insert num into sorted_list maintaining sorted order
        bisect.insort(sorted_list, num)
        n = len(sorted_list)

        if n % 2 == 1:  # Odd length
            median = sorted_list[n // 2]
        else:  # Even length
            median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

        medians.append(median)

    return medians


# Test
stream = [2, 1, 5, 7, 2, 0, 5]
print(running_median(stream))


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
