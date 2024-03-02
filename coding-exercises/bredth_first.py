import random
import Queue

class Node(object):
    def __init__(self, right, left, value):
        self.right_child = right
        self.left_child = left
        self.value = value

    def add_child(self, node):
        if node.value < self.value:
            if self.left_child is None:
                self.left_child = node
            else:
                self.left_child.add_child(node)

        else:
            if self.right_child is None:
                self.right_child = node
            else:
                self.right_child.add_child(node)

numbers = [random.randint(0, 100) for i in range(0,10)]

root = None
for number in numbers:
    if root is None:
        root = Node(None, None, number)
    else:
        root.add_child(Node(None, None, number))

def traverseInOrder(node):
    if node is None:
        return

    traverseInOrder(node.right_child)
    print(node.value)
    traverseInOrder(node.left_child)

print(numbers)
traverseInOrder(root)


def traverseBredthFirst(node):
    q = Queue.Queue()

    q.put(node)
    
    while(not q.empty()):
       next_node = q.get()

       print(next_node.value)

       if next_node.left_child is not None:
           q.put(next_node.left_child)
           
       if next_node.right_child is not None:
           q.put(next_node.right_child)




print("\n BFT \n")

traverseBredthFirst(root)

 