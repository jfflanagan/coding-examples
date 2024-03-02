coins = [1,2,5]
amount = 5

table =  [[0 for j in range(amount + 1)] for i in range(len(coins) + 1)]
for i in range(len(coins) + 1):
    table[i][0] = 1.0

for row in range(1, len(coins)+1):
    for column in range(1, amount + 1):
        without_new_coin = table[row - 1][column]
        with_new_coin_affect = 0
        if column - coins[row - 1] >= 0:
            with_new_coin_affect = table[row][column - coins[row - 1]]

        table[row][column] = without_new_coin + with_new_coin_affect

print table[len(coins)][amount]

def ways(coins, row, column):
    if column == 0:
        return 1.0
    if column > 0 and row == 0:
        return 0.0

    if column - coins[row - 1] >= 0: 
        return ways(coins, row - 1, column) + ways(coins, row, column - coins[row - 1])
    else:
        return ways(coins, row - 1, column)

print ways(coins, 3, 5)