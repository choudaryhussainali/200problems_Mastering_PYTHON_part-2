# 🔹 2. Sum of All Even Numbers in a List
# Write a function that returns the sum of all even numbers from a given list.

# Sample Input: [2, 5, 8, 9, 10]
# Expected Output: 20

def sum_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)

# Sample Input
print(sum_even_numbers([2, 5, 8, 9, 10]))

# Output:
# 20


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
