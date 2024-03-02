#Uses python3

import sys

sys.setrecursionlimit(200000)

class Vetrex(object):
    def __init__(self, index):
        self.index = index
        self.edges = []
        self.visited = False

    def add_edge(self, edge):
        self.edges.append(edge)

    def visit(self):
        self.visited = True

def explore(x, order):
    x.visit()

    for edge in x.edges:
        if not edge.visited:
            explore(edge, order)

    order.append(x.index)

def dfs(adj):
    order = []
    for v in adj:
        if not v.visited:
            explore(v, order)

    order.reverse()

    return order

def number_of_strongly_connected_components(adj, adj_rev):
    result = 0
    order = dfs(adj_rev)
    _ = []
    for index in order:
        if not adj[index - 1].visited:
            result += 1
            explore(adj[index - 1], _)

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    adj = []
    adj_rev = []
    for i in range(n):
        adj.append(Vetrex(i+1))
        adj_rev.append(Vetrex(i+1))

    for (a, b) in edges:
        adj[a - 1].add_edge(adj[b - 1])
        adj_rev[b - 1].add_edge(adj_rev[a - 1])

    print(number_of_strongly_connected_components(adj, adj_rev))
