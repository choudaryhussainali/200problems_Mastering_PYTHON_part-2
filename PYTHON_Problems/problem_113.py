# Problem 113: Rotate a square matrix (list of lists) by 90 degrees clockwise.
# Example: [[1,2,3],[4,5,6],[7,8,9]] → [[7,4,1],[8,5,2],[9,6,3]]

def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))
# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
