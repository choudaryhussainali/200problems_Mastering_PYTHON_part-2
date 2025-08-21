# Given a list of tuples, sort it by the second item in each tuple.


data = [("Apple", 5), ("Banana", 2), ("Mango", 8), ("Orange", 4)]

sort = sorted(data, key=lambda x: x[1])

print(sort)

### OUTPUT [('Banana', 2), ('Orange', 4), ('Apple', 5), ('Mango', 8)]


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
