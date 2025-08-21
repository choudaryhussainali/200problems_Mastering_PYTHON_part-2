#spiral matrix traversal

def spiral_order(matrix):
    result = []
    if not matrix:
        return result

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # 1️⃣ Traverse Left → Right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # 2️⃣ Traverse Top → Bottom
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # 3️⃣ Traverse Right → Left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
