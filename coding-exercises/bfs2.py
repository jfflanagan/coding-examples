#Uses python3

import sys
import queue

class Vetrex(object):
    def __init__(self, index):
        self.index = index
        self.edges = []
        self.distance = -1

    def add_edge(self, edge):
        self.edges.append(edge)


def distance(adj, s, t):
    q = queue.Queue()

    start = adj[s - 1]
    start.distance = 0
    q.put(start)

    destination = adj[t - 1]

    while not q.empty():
        current = q.get()

        for next_vertex in current.edges:
            if next_vertex.distance == -1:
                next_vertex.distance = current.distance + 1
                q.put(next_vertex)

    return destination.distance

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    adj = []
    for i in range(n):
        adj.append(Vetrex(i+1))

    for (a, b) in edges:
        adj[a - 1].add_edge(adj[b - 1])
        adj[b - 1].add_edge(adj[a - 1])

    s, t = data[2 * m], data[2 * m + 1]
    print(distance(adj, s, t))
