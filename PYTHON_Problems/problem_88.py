# Exercise 8: Type-Based List Operations

# Ask the user to input 6 values of any type. Then:

# Create a list of all numeric values.

# Create a list of all string values.

# Multiply all numeric values together.

# Concatenate all string values into a single string.

values = [input(f"Enter value {i+1}: ") for i in range(6)]

numeric_list = []
string_list = []

for v in values:
    try:
        num = int(v)
        numeric_list.append(num)
    except ValueError:
        try:
            num = float(v)
            numeric_list.append(num)
        except ValueError:
            string_list.append(v)

# Multiply all numeric values
product = 1
for num in numeric_list:
    product *= num

# Concatenate all strings
concat_str = "".join(string_list)

print("Numeric list:", numeric_list)
print("String list:", string_list)
print("Product of numeric values:", product)
print("Concatenated string:", concat_str)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
