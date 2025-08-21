# Problem 163
# Convert a list of dictionaries into a dictionary grouped by a given key.
def group_by_key(lst: list, key: str):
    grouped = {}
    for item in lst:
        grouped.setdefault(item[key], []).append(item)
    return grouped

# Example
students = [
    {"name": "Ali", "grade": "A"},
    {"name": "Sara", "grade": "B"},
    {"name": "John", "grade": "A"},
]
print(group_by_key(students, "grade"))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
