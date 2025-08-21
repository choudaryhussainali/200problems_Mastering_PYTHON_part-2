# Problem 162
# Given a dictionary of products and their prices, apply a discount dictionary to update the prices.
def apply_discounts(prices: dict, discounts: dict):
    updated = {}
    for product, price in prices.items():
        if product in discounts:
            updated[product] = round(price * (1 - discounts[product]/100), 2)
        else:
            updated[product] = price
    return updated

# Example
print(apply_discounts({"apple": 100, "banana": 50}, {"apple": 10}))

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
