#Uses python3
import sys
import math

class Edge(object):
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

class DisjointSets(object):
    def __init__(self, num_sets):
        self.disjoint_sets = [i for i in range(num_sets)]
        self.rank = [0]*num_sets
        self.num_sets = num_sets

    def find(self, i):
        while self.disjoint_sets[i] != i:
           i = self.disjoint_sets[i] 

        return self.disjoint_sets[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id != j_id:
            self.num_sets -= 1

            if self.rank[i_id] > self.rank[j_id]:
                self.disjoint_sets[j_id] = self.disjoint_sets[i_id]
            if self.rank[j_id] > self.rank[i_id]:
                self.disjoint_sets[i_id] = self.disjoint_sets[j_id]
            if self.rank[j_id] == self.rank[i_id]:
                self.disjoint_sets[j_id] = self.disjoint_sets[i_id]
                self.rank[i_id] += 1

    
def clustering(x, y, k):
    edges = []

    assert len(x) == len(y)

    # compute all possible edges (triangular matrix)
    num_points = len(x)
    edges = []
    for i in range(num_points):
        for j in range(i + 1, num_points):
            distance = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
            edges.append(Edge(i, j, distance))

    
    ds = DisjointSets(len(x))

    edges.sort(key=lambda x: x.weight)
    for edge in edges:

        if ds.find(edge.u) != ds.find(edge.v):
            if ds.num_sets == k:
                return edge.weight

            ds.union(edge.u, edge.v)

    return -1.

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
