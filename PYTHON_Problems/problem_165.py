# Problem 165
# Given a dictionary of employee -> salary, return the average salary of each department.
def avg_salary_by_dept(data: dict):
    dept_totals = {}
    dept_counts = {}
    for emp, (dept, salary) in data.items():
        dept_totals[dept] = dept_totals.get(dept, 0) + salary
        dept_counts[dept] = dept_counts.get(dept, 0) + 1
    return {dept: round(dept_totals[dept]/dept_counts[dept], 2) for dept in dept_totals}

# Example
employees = {
    "Ali": ("IT", 5000),
    "Sara": ("HR", 4000),
    "John": ("IT", 6000)
}
print(avg_salary_by_dept(employees))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
