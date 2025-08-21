# Input: A list of integers
# Output: A list containing squares of only the even numbers
# Use list comprehension

# Example: [1, 2, 3, 4] → [4, 16]


def even_square(a):
    b = [x**2 for x in a if x%2==0]
    return b


c = even_square([1,2,3,4,5,6,7,8,9,23,45,67,78,34,23])
print(c)



# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
