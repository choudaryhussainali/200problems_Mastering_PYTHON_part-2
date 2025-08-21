# Write a function to return the names of top scorers (highest score) in alphabetical order.



students = [
    {"name": "Ali", "score": 88},
    {"name": "Sara", "score": 95},
    {"name": "Bilal", "score": 75},
    {"name": "Ayesha", "score": 95}
]


def top_scorers(students):
    # Find the highest score
    max_score = max(student["score"] for student in students)
    
    # Get names of students who have the highest score
    top_names = [student["name"] for student in students if student["score"] == max_score]
    
    # Return names in alphabetical order
    return sorted(top_names)


# Test
students = [
    {"name": "Ali", "score": 88},
    {"name": "Sara", "score": 95},
    {"name": "Bilal", "score": 75},
    {"name": "Ayesha", "score": 95}
]

print(top_scorers(students))  


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
