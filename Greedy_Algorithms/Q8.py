def candy_store(prices, N, K):
    prices.sort()
    min_cost = prices[-1]
    max_cost = sum(prices)
    return min_cost, max_cost