#Uses python3

import sys

class Vetrex(object):
    def __init__(self, index):
        self.index = index
        self.edges = []
        self.visited = False
        self.return_edge = False

    def add_edge(self, edge):
        self.edges.append(edge)

    def visit(self):
        self.visited = True

def is_acylic(x):
    x.return_edge = True        
    x.visit()

    for edge in x.edges:
        if edge.return_edge:
            return True
        if not edge.visited:
            if is_acylic(edge):
                return True

    x.return_edge = False

    return False

def acyclic(adj):
    for v in adj:
        if not v.visited:
            if is_acylic(v):
                return 1
    return 0

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

    print(acyclic(adj))
