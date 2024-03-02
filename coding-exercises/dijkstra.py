#Uses python3

import sys
import heapq

class Vetrex(object):
    def __init__(self, index):
        self.index = index
        self.edges = []
        self.distance = float('inf')
        self.best_distance = False

    def add_edge(self, edge, weight):
        self.edges.append((edge, weight))

def distance(adj, s, t):
    adj[s - 1].distance = 0

    pq = [(v.distance, v.index - 1) for v in adj]
    heapq.heapify(pq)

    while pq:
        _, u_index = heapq.heappop(pq)
        u = adj[u_index]
        if u.best_distance:
            continue

        u.best_distance = True

        for edge, weight in u.edges:
            if edge.distance > u.distance + weight:
                edge.distance = u.distance + weight

                heapq.heappush(pq, (edge.distance, edge.index - 1))

    if adj[t - 1].distance == float('inf'):
        return -1
    else:
        return adj[t - 1].distance


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]

    adj = []
    for i in range(n):
        adj.append(Vetrex(i+1))

    for ((a, b), w) in edges:
        adj[a - 1].add_edge(adj[b - 1], w)

    s, t = data[0], data[1]
    print(distance(adj, s, t))
