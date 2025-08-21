# Problem 180
# Given a dict of city->population, return the top 3 cities with population in descending order.
def top_cities(d: dict, n=3):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)[:n]

# Example
print(top_cities({"NY": 8500000, "LA": 4000000, "Chicago": 2700000, "Houston": 2300000}, 3))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
