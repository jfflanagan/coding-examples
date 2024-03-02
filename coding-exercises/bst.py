import random

class Node(object):
    def __init__(self, right_child, left_child, value):
        self.right_child = right_child
        self.left_child = left_child
        self.value = value

    def add_node(self, node):
        if node.value > self.value:
            if self.right_child is None:
                self.right_child = node
            else:
                self.right_child.add_node(node)
        else:
            if self.left_child is None:
                self.left_child = node
            else:
                self.left_child.add_node(node)


numbers = [random.randint(0,100) for i in range(0,10)]
print(numbers)

# Populate tree
root = None
for number in numbers:
    node = Node(None, None, number)

    if root is None:
        root = node
    else:
       root.add_node(node)

# Traverse tree
def traverse_tree(node, sorted_list):
    if node.right_child is not None:
        traverse_tree(node.right_child, sorted_list)

    sorted_list.append(node.value)

    if node.left_child is not None:
        traverse_tree(node.left_child, sorted_list)

sorted_list = []
traverse_tree(root, sorted_list)

print(sorted_list)


    





