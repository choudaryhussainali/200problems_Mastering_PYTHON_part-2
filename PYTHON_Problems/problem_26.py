#  Mini Project – Guess the Number Game 

import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number (1–100): "))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {attempts} tries.")
        break


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
