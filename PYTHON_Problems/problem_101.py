# Exercise 21: Odd-Even String Transformer

# Take 5 numeric strings from the user. Convert them to numbers.

# If a number is even → convert it to string with prefix "E_".

# If a number is odd → convert it to string with prefix "O_".
# Print the final list of transformed strings.

values = [input(f"Enter numeric string {i+1}: ") for i in range(5)]
transformed = []

for v in values:
    try:
        num = int(v)
        if num % 2 == 0:
            transformed.append("E_" + str(num))
        else:
            transformed.append("O_" + str(num))
    except ValueError:
        print(f"'{v}' is not a valid integer. Ignored.")

print("Transformed list:", transformed)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
