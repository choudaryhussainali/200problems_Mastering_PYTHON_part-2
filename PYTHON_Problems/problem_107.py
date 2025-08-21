# Exercise 27: Type-Based Sorting Challenge

# Take 10 inputs (numbers or strings). Convert numeric strings to numbers. Then:

# Sort numbers ascending

# Sort strings descending

# Print two separate sorted lists


values = [input(f"Enter value {i+1}: ") for i in range(10)]
numbers = []
strings = []

for v in values:
    try:
        num = int(v)
        numbers.append(num)
    except ValueError:
        try:
            num = float(v)
            numbers.append(num)
        except ValueError:
            strings.append(v)

numbers.sort()
strings.sort(reverse=True)

print("Sorted numbers (asc):", numbers)
print("Sorted strings (desc):", strings)



# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
