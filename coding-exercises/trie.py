#Uses python3
import sys

class Node(object):
    def __init__(self, index):
        self.children = {}
        self.index = index

def build_trie(patterns):
    current_index = 0
    tree = Node(current_index)
    tree_list = []

    for pattern in patterns:
        current_node = tree
        for c in pattern:
            if c in current_node.children:
                current_node = current_node.children[c]
            else:
                tree_list.append("{}->{}:{}".format(current_node.index, current_index + 1, c))
                current_index += 1
                current_node.children[c] = Node(current_index)
                                current_node = current_node.children[c]

    return tree_list

if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for item in tree:
        print(item)

