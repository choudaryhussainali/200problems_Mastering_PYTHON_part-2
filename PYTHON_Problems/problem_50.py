# Task:
# Write a countdown timer in seconds.
# Input: Enter countdown time: 5
# Output:
# 5... 4... 3... 2... 1... Time’s up!

import time

def countdown(seconds):
    while seconds:
        print(seconds, end="... ", flush=True)
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

countdown(5)


# 5... 4... 3... 2... 1... Time's up!



# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
