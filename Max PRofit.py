def maxProfit(prices, k):
    if not len(prices):
        return 0
    evenProfit = [0 for d in prices]
    oddProfit = [0 for d in prices]
    for t in range(1, k + 1):
        return evenProfit[-1] if k % 2 == 0 else oddProfit[-1]