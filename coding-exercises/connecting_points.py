#Uses python3
import sys
import math

class Vetrex(object):
    def __init__(self, point):
        self.point = point
        self.visited = False
        self.best_distance = float('inf')

# use array implementation because this is a complete graph
def get_min(adj):
    best_distance = float('inf')
    best_item = None
    for item in adj:
        if not item.visited:
            if item.best_distance < best_distance:
                best_distance = item.best_distance
                best_item = item

    return best_item


def minimum_distance(x, y):
    adj = []
    for point in zip(x,y):
        adj.append(Vetrex(point))

    adj[0].best_distance = 0

    total_distance = 0

    current_item = adj[0]
    while current_item is not None:
        total_distance += current_item.best_distance
        current_item.visited = True
        for item in adj:
            if item.visited: # already processed this index. This would be a cycle
                continue
            distance = math.sqrt((current_item.point[0] - item.point[0])**2 + (current_item.point[1] - item.point[1])**2)
            if item.best_distance > distance:
                item.best_distance = distance
        
        current_item = get_min(adj)

    return total_distance


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
