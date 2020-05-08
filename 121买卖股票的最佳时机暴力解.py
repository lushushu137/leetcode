def maxProfit(prices) -> int:
    profit = 0
    for buy in range(len(prices)):
        for sell in range(buy, len(prices)):
            profit = max(prices[sell] - prices[buy], profit)
    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
