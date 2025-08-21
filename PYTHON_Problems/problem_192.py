# Problem 192
# Use a lambda to sort a list of dicts by a computed value (price * quantity).
products = [{"item": "apple", "price": 2, "qty": 5},
            {"item": "banana", "price": 1, "qty": 12},
            {"item": "cherry", "price": 3, "qty": 4}]
sorted_products = sorted(products, key=lambda x: x["price"] * x["qty"], reverse=True)
print(sorted_products)

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
