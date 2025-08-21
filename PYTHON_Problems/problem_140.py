# Problem 140: Find the median of two sorted lists without merging them.
def find_median_sorted_arrays(nums1, nums2):
    A, B = nums1, nums2
    if len(A) > len(B): A, B = B, A
    m, n = len(A), len(B)
    imin, imax, half = 0, m, (m+n+1)//2
    while imin <= imax:
        i = (imin+imax)//2
        j = half - i
        if i < m and B[j-1] > A[i]:
            imin = i+1
        elif i > 0 and A[i-1] > B[j]:
            imax = i-1
        else:
            if i == 0: max_left = B[j-1]
            elif j == 0: max_left = A[i-1]
            else: max_left = max(A[i-1], B[j-1])
            if (m+n) % 2 == 1:
                return max_left
            if i == m: min_right = B[j]
            elif j == n: min_right = A[i]
            else: min_right = min(A[i], B[j])
            return (max_left + min_right) / 2.0

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
