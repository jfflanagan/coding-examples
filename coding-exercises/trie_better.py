#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    current_index = 0
    tree = {0:{}}

    for pattern in patterns:
        current_node = tree[0]
        for c in pattern:
            if c in current_node:
                current_node = tree[current_node[c]]
            else:
                current_index += 1
                current_node[c] = current_index # add a new node reference to children of current node
                tree[current_index] = {} # add the actual node now
                current_node = tree[current_index] # update the current working node

    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
