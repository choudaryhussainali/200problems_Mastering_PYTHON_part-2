# # Example
# nums = [1, 2, 2, 3, 4, 4, 5]
# remove duplicates

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

data = [1, 2, 2, 3, 1, 4, 3]
print(remove_duplicates(data))  # [1, 2, 3, 4]

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
