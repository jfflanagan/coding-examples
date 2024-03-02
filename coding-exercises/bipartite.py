#Uses python3

import sys
import queue

class Vetrex(object):
    def __init__(self, index):
        self.index = index
        self.edges = []
        self.visited = False
        self.color = -1

    def add_edge(self, edge):
        self.edges.append(edge)

def bipartite(adj):
    q = queue.Queue()

    # trivaial case with only one vetrex. Cannot be divided into two sets
    if len(adj) < 2:
        return 0

    for v in adj:
        if v.visited:
            continue

        start = v
        start.color = 0
        q.put(start)

        while not q.empty():
            current = q.get()
            current.visited = True

            for next_vertex in current.edges:
                if not next_vertex.visited:
                    next_vertex.color = (current.color + 1) % 2
                    q.put(next_vertex)
                else:
                    if current.color == next_vertex.color:
                        return 0

    return 1

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

    print(bipartite(adj))
