from data import coin_set


def find_coins_greedy(amount: int):
    balance = amount
    index = 0
    result_set = {}

    while index < len(coin_set) and balance > 0:
        coin_quantity = balance // coin_set[index]

        if coin_quantity != 0:
            result_set[coin_set[index]] = coin_quantity
            balance -= coin_set[index] * coin_quantity

        index += 1

    return result_set
