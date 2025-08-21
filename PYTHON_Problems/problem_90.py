# Exercise 10: Dynamic Type Calculator

# Ask the user to input two values. Based on their types:

# If both are integers → perform integer division and modulo.

# If both are floats → perform floor division and exponentiation.

# If one is int and the other is float → perform addition, subtraction, multiplication, and division.
# Goal: Logical branching + type conversion + arithmetic operations.

def convert(val):
    try:
        return int(val)
    except ValueError:
        try:
            return float(val)
        except ValueError:
            return None

a = convert(input("Enter first value: "))
b = convert(input("Enter second value: "))

if a is None or b is None:
    print("Invalid input! Numbers required.")
else:
    if isinstance(a, int) and isinstance(b, int):
        print("Integer division:", a // b if b != 0 else "Division by zero!")
        print("Modulo:", a % b if b != 0 else "Division by zero!")
    elif isinstance(a, float) and isinstance(b, float):
        print("Floor division:", a // b if b != 0 else "Division by zero!")
        print("Exponentiation:", a ** b)
    else:
        print("Addition:", a + b)
        print("Subtraction:", a - b)
        print("Multiplication:", a * b)
        print("Division:", a / b if b != 0 else "Division by zero!")


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
