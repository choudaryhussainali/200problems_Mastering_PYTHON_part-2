# Problem 151
# Given a dictionary of students and their scores, return the names of the top 3 scorers.
# If there are ties, include all tied students.

def top_3_scorers(scores: dict):
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_scores = []
    cutoff = None
    for name, score in sorted_scores:
        if len(top_scores) < 3:
            top_scores.append(name)
            cutoff = score
        elif score == cutoff:
            top_scores.append(name)
    return top_scores

# Example
print(top_3_scorers({"Ali": 90, "Sara": 85, "John": 95, "Mary": 95, "Tom": 88}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
