# python3

# python3
from queue import Queue

class Edge:

    def __init__(self, u, v, capacity, id):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0
        self.id = id

class Node:
    def __init__(self):
        self.visited = False
        self.previous = None
        self.edges = []

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.nodes = [Node() for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        num_edges = len(self.edges)

        forward_edge = Edge(from_, to, capacity, num_edges)
        backward_edge = Edge(to, from_, 0, num_edges + 1)

        self.edges.append(forward_edge)
        self.edges.append(backward_edge)

        self.nodes[from_].edges.append(num_edges)
        self.nodes[to].edges.append(num_edges + 1)

    def size(self):
        return len(self.nodes)

    def get_ids(self, from_):
        return self.nodes[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow

def bfs(graph):
    source = graph.nodes[0]
    sink_id = len(graph.nodes) - 1

    q = Queue()
    q.put(source)

    while not q.empty():
        current = q.get()
        current.visited = True
        for edge_id in current.edges:
            edge = graph.edges[edge_id] 

            if(edge.capacity - edge.flow) > 0:

                if edge.v == sink_id:
                    graph.nodes[edge.v].previous = edge_id
                    return True

                if not graph.nodes[edge.v].visited:
                    graph.nodes[edge.v].previous = edge_id
                    q.put(graph.nodes[edge.v])

    return False

def find_min_capacity(graph):
    sink_id = len(graph.nodes) - 1

    min_capacity = 1e9
    previous_edge_id = graph.nodes[sink_id].previous
    while previous_edge_id is not None:
        previous_edge = graph.edges[previous_edge_id]
        res_capacity = previous_edge.capacity - previous_edge.flow
        min_capacity = min(min_capacity, res_capacity)
        previous_edge_id = graph.nodes[previous_edge.u].previous 

    if min_capacity < 1e9:
         return min_capacity
    else:
        return None

def update_flow(graph, flow):
    sink_id = len(graph.nodes) - 1

    previous_edge_id = graph.nodes[sink_id].previous
    while previous_edge_id is not None:
        previous_edge = graph.edges[previous_edge_id]
        graph.add_flow(previous_edge_id, flow)

        previous_edge_id = graph.nodes[previous_edge.u].previous  

def resest(graph):
    for node in graph.nodes:
        node.visited = False
        node.previous = None

def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def max_flow(graph, from_, to):
    flow = 0
    while True:
        if not bfs(graph):
            return flow
        
        min_capacity = find_min_capacity(graph)
        update_flow(graph, min_capacity)
        resest(graph)

        flow += min_capacity
    
    return flow

class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return n, m, adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x) for x in matching]
        print(' '.join(line))

    def find_matching(self, graph, n, m):
        matching = [-1] * n

        for edge in graph.edges:
            if edge.u >= 1 and edge.u <= n and edge.v >= n + 1 and edge.v <= n + m:
                if edge.flow == 1:
                    matching[edge.u - 1] = edge.v - n

        return matching

    def solve(self):
        n, m, adj_matrix = self.read_data()

        graph = FlowGraph(n + m + 2)
        for i in range(n):
            graph.add_edge(0, i + 1, 1)
            for j in range(m):
                if adj_matrix[i][j] == 1:
                    graph.add_edge(i + 1, n + j + 1, 1)

        for j in range(m):
            graph.add_edge(n + j + 1, n + m + 1, 1)

        max_flow(graph, 0, graph.size() - 1)

        matching = self.find_matching(graph, n, m)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
