# Task:
# Simulate a dice roll using random.randint(1, 6).
# Repeat until the user types "no".

# Sample Output:
# Dice rolled: 4
# Roll again? yes
# Dice rolled: 2
# Roll again? no


import random

while True:
    roll = random.randint(1, 6)
    print(f"Dice rolled: {roll}")
    again = input("Roll again? (yes/no): ").lower()
    if again != "yes":
        break


# Dice rolled: 3
# Roll again? yes
# Dice rolled: 6
# Roll again? no


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
