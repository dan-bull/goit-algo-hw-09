
def find_coins_greedy(amount, coins=[50, 20, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        while amount >= coin:
            result[coin] = result.get(coin, 0) + 1
            amount -= coin
    return result

coins_greedy = find_coins_greedy(113)
print(coins_greedy)
