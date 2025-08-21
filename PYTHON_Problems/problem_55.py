# # Example
# nested_list = [[1, 2], [3, 4], [5, 6]]
# # Output: [1, 2, 3, 4, 5, 6]

def flatten(lists):
    return [item for sublist in lists for item in sublist]



nested_list = [[1, 2], [3, 4], [5, 6]]
flatten(nested_list)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
