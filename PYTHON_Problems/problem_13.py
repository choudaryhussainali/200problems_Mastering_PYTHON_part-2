# Input:
# keys = ['name', 'age', 'city']
# values = ['Hussain', 21, 'Lahore']
# Output:
# {'name': 'Hussain', 'age': 21, 'city': 'Lahore'}

# Use dict comprehension or zip()

## SOLUTION 1 

keys = ['name', 'age', 'city']
values = ['Hussain', 21, 'Lahore']
dict = {}
for i, j in zip(keys, values):
    dict[i] = j


print(dict)

## SOLUTION 2

def lists_to_dict(keys, values):
    return {k: v for k, v in zip(keys, values)}

# Sample Input

keys = ['name', 'age', 'city']
values = ['Hussain', 21, 'Lahore']
print(lists_to_dict(keys, values))


# Output:
# {'name': 'Hussain', 'age': 21, 'city': 'Lahore'}



# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
