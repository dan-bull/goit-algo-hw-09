
def find_min_coins(amount, coins=[50, 20, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coins_used = [{}] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i] > dp[i - coin] + 1:
                dp[i] = dp[i - coin] + 1
                coins_used[i] = {**coins_used[i - coin], coin: coins_used[i - coin].get(coin, 0) + 1}

    return coins_used[amount]

coins_dp = find_min_coins(113)
print(coins_dp) 