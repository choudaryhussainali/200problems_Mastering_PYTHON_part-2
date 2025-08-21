# Problem 171
# Given a dictionary of student->marks, return the top k students with highest marks.
def top_k_students(marks: dict, k: int):
    return sorted(marks.items(), key=lambda x: x[1], reverse=True)[:k]

# Example
print(top_k_students({"Ali": 85, "Sara": 92, "John": 78, "Mary": 95}, 2))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
