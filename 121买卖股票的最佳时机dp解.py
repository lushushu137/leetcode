def maxProfit(prices):
    currMax = 0
    tempMin = min(prices[0], prices[1])
    currMax = max(0, prices[1] - prices[0])
    for i in range(2, len(prices)):
        tempMin = min(tempMin, prices[i])
        notSellToday = currMax
        sellToday = prices[i] - tempMin
        currMax = max(notSellToday, sellToday)
    return currMax


print(maxProfit([7, 1, 5, 3, 6, 4]))
