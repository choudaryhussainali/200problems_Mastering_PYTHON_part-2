# 🔹 4. Find All Prime Numbers up to N
# Take an integer n and print all prime numbers from 2 to n.

# Sample Input: n = 10
# Expected Output: 2, 3, 5, 7

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_up_to_n(n):
    return [i for i in range(2, n+1) if is_prime(i)]

# Sample Input
print(prime_up_to_n(10))

# Output:
# [2, 3, 5, 7]


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
