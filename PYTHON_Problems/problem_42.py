# Task:
# Write a function to generate a strong random password of given length.
# Use letters (upper & lower), digits, and special characters.

# Sample Input: generate_password(10)
# Expected Output: A random 10-character secure password like: a$9D@kZ7!c

import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Sample:
print(generate_password(10))

# Output: Random strong password like → D$5g!2kL@Z


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
