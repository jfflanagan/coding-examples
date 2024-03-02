#Uses python3

import sys

def negative_cycle(adj, edges):

    for _ in range(len(adj) - 1):
        for edge in edges:
            if adj[edge[1]] > adj[edge[0]] + edge[2]:
                adj[edge[1]] = adj[edge[0]] + edge[2]

    for edge in edges:
        if adj[edge[1]] > adj[edge[0]] + edge[2]:
            return 1 

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]

    adj = []
    my_edges = []
    for i in range(n):
        adj.append(0) # Starting point to find a negative cycle could be from any vertex. Rather then checking them all(expensive) just define them all as a starting point.

    for ((a, b), w) in edges:
        my_edges.append((a-1, b-1, w))

    print(negative_cycle(adj, my_edges))
