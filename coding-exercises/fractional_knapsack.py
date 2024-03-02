# Uses python3
import sys
from collections import namedtuple

Item = namedtuple('Item', 'density, weight')

def get_optimal_value(capacity, weights, values):
    value = 0.

    densities = [Item(value/weight, weight) for value, weight in zip(values, weights)]
    densities.sort(key=lambda x: x.density, reverse=True)

    for item in densities:
        item_amount = min(capacity, item.weight)
        value += item.density * item_amount
        capacity -= item_amount

        if capacity == 0:
            break 

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
