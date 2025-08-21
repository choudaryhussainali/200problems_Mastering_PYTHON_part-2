# 🔸 1. Read and Write to a File
# Task:
# Write a program that:
# Takes 5 names from the user
# Writes them to a text file names.txt
# Then reads and displays the names from the file

# Write names to file
names = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

with open("names.txt", "w") as f:
    for name in names:
        f.write(name + "\n")

print("Names saved successfully!")

# Read from file
print("Reading from file:")
with open("names.txt", "r") as f:
    for i, line in enumerate(f.readlines(), start=1):
        print(f"{i}. {line.strip()}")


    


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
