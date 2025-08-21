# Write a function to calculate factorial of a number using recursion.

# Input: 5
# Output: 120 (5*4*3*2*1)


def Factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
            
            return num * Factorial(num-1)


print(Factorial(5))



# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
