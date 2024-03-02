# Uses python3
import sys

def optimal_weight(W, w):
    dp_table = [[0]*(W + 1) for i in range(len(w)+1)]

    
    for j in range(1, W + 1):
        for i in range(1, len(w) + 1):
            with_item = 0
            if j - w[i - 1] >= 0:
                with_item = dp_table[i - 1][j - w[i - 1]] + w[i - 1]

            without_item = dp_table[i - 1][j]
 
            best_val = max(with_item, without_item)

            dp_table[i][j] = best_val

    return dp_table[len(w)][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
