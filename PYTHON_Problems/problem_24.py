# Ali - Average: 85.0
# Sara - Average: 86.0
# Zoya - Average: 75.67

students = {
    "Ali": {"Math": 90, "English": 80, "Science": 85},
    "Sara": {"Math": 88, "English": 92, "Science": 78},
    "Zoya": {"Math": 75, "English": 70, "Science": 82}
}

for name, marks in students.items():
    avg = sum(marks.values())/len(marks)
    print(f"{name} - Average: {avg}")

    

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
