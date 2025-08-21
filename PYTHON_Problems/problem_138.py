# Problem 138: Given a list of stock prices, find the maximum profit from at most two transactions.
def max_profit(prices):
    buy1 = buy2 = float('inf')
    profit1 = profit2 = 0
    for price in prices:
        buy1 = min(buy1, price)
        profit1 = max(profit1, price - buy1)
        buy2 = min(buy2, price - profit1)
        profit2 = max(profit2, price - buy2)
    return profit2

# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
