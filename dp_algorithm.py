from data import coin_set


def find_min_coins(amount: int):
    dp_set = [0] + [float("inf")] * amount
    last = [0] * (amount + 1)

    for i in range(1, amount + 1):
        best = dp_set[i]
        best_coin = 0

        for coin in coin_set:
            if coin <= i:
                candidate = dp_set[i - coin] + 1
                if candidate < best:
                    best = candidate
                    best_coin = coin

        dp_set[i] = best
        last[i] = best_coin

    result = {}
    balance = amount

    while balance > 0:
        coin = last[balance]

        result[coin] = result.get(coin, 0) + 1
        balance -= coin

    return result
