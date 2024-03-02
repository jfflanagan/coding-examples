#Uses python3

import sys

class Vetrex(object):
    def __init__(self, index):
        self.index = index
        self.edges = []
        self.visited = False

    def add_edge(self, edge):
        self.edges.append(edge)

    def visit(self):
        self.visited = True

def dfs(x, order):
    x.visit()

    for edge in x.edges:
        if not edge.visited:
            dfs(edge, order)

    order.append(x.index)

def toposort(adj):
    order = []
    for v in adj:
        if not v.visited:
            dfs(v, order)

    order.reverse()
    return order

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

    order = toposort(adj)
    for x in order:
        print(x, end=' ')

