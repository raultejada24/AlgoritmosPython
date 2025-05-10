
def money_exchange(value, coins):
    n = len(coins)-1
    exchange = [0] * (len(coins))
    while value > 0 and n >= 0:
        exchange[n] = value // coins[n]
        value = value % coins[n]
        n -= 1
    return exchange

coins = [1, 2, 5, 10, 20, 50, 100, 200, 500]
value = 250
exchange = money_exchange(value, coins)
print(exchange)
