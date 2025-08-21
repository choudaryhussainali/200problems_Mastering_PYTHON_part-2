# Exercise 14: Type-Based Decision Maker

# Ask the user to input a value. Then:

# If it’s an integer → check if prime.

# If it’s a float → round to nearest integer.

# If it’s a string → print first and last characters.

# Otherwise → print "Unsupported type"

value = input("Enter a value: ")

# Try integer
try:
    num = int(value)
    # Check prime
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(num, "is not prime")
                break
        else:
            print(num, "is prime")
    else:
        print(num, "is not prime")
except ValueError:
    # Try float
    try:
        num = float(value)
        print("Rounded float:", round(num))
    except ValueError:
        # String
        if isinstance(value, str):
            if len(value) >= 1:
                print("First character:", value[0])
                print("Last character:", value[-1])
            else:
                print("Empty string")
        else:
            print("Unsupported type")


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
