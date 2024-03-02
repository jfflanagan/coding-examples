# Uses python3
import sys

def get_change(m):
    coins = [1,3,4]
    dp_table = [0] * (m + 1)

    for i in range(1, m + 1):
        min_coins = float('inf')
        num_coins = 0
        for coin in coins:
            if i - coin > -1:
                num_coins = dp_table[i - coin] + 1

                if num_coins < min_coins:
                    min_coins = num_coins

            dp_table[i] = min_coins
            
    return dp_table[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
