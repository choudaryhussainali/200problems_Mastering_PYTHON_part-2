# Problem 124
# Given a list of stock prices, find the maximum profit you can achieve by buying and selling once.
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)
    return max_profit

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
