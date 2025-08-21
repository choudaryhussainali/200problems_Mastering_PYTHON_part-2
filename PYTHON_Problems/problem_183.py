# Problem 183
# Use a lambda with filter() to extract only prime numbers from a list.
nums = [2, 3, 4, 5, 10, 11, 15, 17]
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
primes = list(filter(is_prime, nums))
print(primes)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
