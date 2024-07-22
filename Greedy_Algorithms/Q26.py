def minCoins(coins, V):
    dp = [float('inf')] * (V + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, V + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[V] if dp[V] != float('inf') else -1


coins = [9, 6, 5, 1]
V = 11
print(minCoins(coins, V)) 