#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node(object):
    def __init__(self, value, left, right):
        self.value = value 
        self.left = left
        self.right = right

def buildTree(treeList, index):
    if index == -1 or not treeList:
        return None

    return Node(treeList[index][0], buildTree(treeList, treeList[index][1]), buildTree(treeList, treeList[index][2]))

def inOrderTraversal(root, result):
    if root is None:
        return True

    isBst = inOrderTraversal(root.left, result)
    if not isBst:
        return False

    result.append(root.value)
    if len(result) > 1 and result[-2] >= result[-1]:
        return False

    return inOrderTraversal(root.right, result)

def IsBinarySearchTree(root):
    # Implement correct algorithm here
    result = []

    return inOrderTraversal(root, result)

def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    root = buildTree(tree, 0)

    if IsBinarySearchTree(root):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()