# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node(object):
    def __init__(self, value, left, right):
        self.value = value 
        self.left = left
        self.right = right

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrderTraversal(self, root, result):
        if root is None:
            return 

        self.inOrderTraversal(root.left, result)
        result.append(root.value)
        self.inOrderTraversal(root.right, result)

    def inOrder(self, root):
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.inOrderTraversal(root, result)    
        return result

    def preOrderTraversal(self, root, result):
        if root is None:
            return 

        result.append(root.value)
        self.preOrderTraversal(root.left, result)   
        self.preOrderTraversal(root.right, result)

    def preOrder(self, root):
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.preOrderTraversal(root, result)  
        return result

    def postOrderTraversal(self, root, result):
        if root is None:
            return 

        self.postOrderTraversal(root.left, result)   
        self.postOrderTraversal(root.right, result)
        result.append(root.value)

    def postOrder(self, root):
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.postOrderTraversal(root, result)
        return result

    def buildTree(self, index):
        if index == -1:
            return None

        return Node(self.key[index], self.buildTree(self.left[index]), self.buildTree(self.right[index]) )

def main():
    tree = TreeOrders()
    tree.read()
    root = tree.buildTree(0)

    print(" ".join(str(x) for x in tree.inOrder(root)))
    print(" ".join(str(x) for x in tree.preOrder(root)))
    print(" ".join(str(x) for x in tree.postOrder(root)))

threading.Thread(target=main).start()