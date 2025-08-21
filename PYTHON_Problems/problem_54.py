# # Example
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# # Output: [3, 4]
def common_elements(list1, list2):
    return list(set(list1) & set(list2))

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(common_elements(a, b))  # [3, 4]


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
