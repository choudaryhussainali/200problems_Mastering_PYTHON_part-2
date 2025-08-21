# Exercise 5: Smart Calculator Input

# Create a program that asks the user to enter two numbers. The program should:

# Convert them to the most appropriate type automatically (int if possible, else float).

# Perform addition, subtraction, multiplication, and division.

# Print the type of result for each operation.
# Goal: Handling input dynamically + type conversion + arithmetic operations.

def convert_input(val):
    try:
        return int(val)
    except ValueError:
        try:
            return float(val)
        except ValueError:
            return None

a = convert_input(input("Enter first number: "))
b = convert_input(input("Enter second number: "))

if a is None or b is None:
    print("Invalid input, numbers required!")
else:
    print("Addition:", a + b, "Type:", type(a + b))
    print("Subtraction:", a - b, "Type:", type(a - b))
    print("Multiplication:", a * b, "Type:", type(a * b))
    if b != 0:
        print("Division:", a / b, "Type:", type(a / b))
    else:
        print("Division by zero is not allowed!")


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
