# Sort a list of student dictionaries by marks.

students = [
    {"name": "Ali", "marks": 87},
    {"name": "Sara", "marks": 92},
    {"name": "Hassan", "marks": 75}
]

sorted_list = sorted(students,  key=lambda x: x["marks"])
print(sorted_list)


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
