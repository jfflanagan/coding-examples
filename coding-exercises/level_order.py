# Definition for a binary tree node.
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if root is None:
        return [[]]

    q = Queue()
    results = []
    resuts_level = []
    current_level = 0

    q.put((root, 0))
    while not q.empty():
        current, level = q.get()
        
        if current is not None:
            if level > current_level:
                results.append(resuts_level[:])
                resuts_level = []
            resuts_level.append(current.val)
            current_level = level

            q.put((current.left, level + 1))
            q.put((current.right, level + 1))
    
    results.append(resuts_level)

    return results

def zig_zag(root):
    s1 = []
    s2 = []
    current_level = 0
    results = []
    resuts_level = []

    s1.append((root, 0))

    while s1 or s2:
        current, level = s1.pop()

        if current is not None:
            if level > current_level:
                results.append(resuts_level[:])
                resuts_level = []

            resuts_level.append(current.val)
            current_level = level
            if level % 2:
                s2.append((current.right, level + 1))
                s2.append((current.left, level + 1))
            else:
                s2.append((current.left, level + 1))
                s2.append((current.right, level + 1))

        if not s1:
            temp = s1
            s1 = s2
            s2 = temp
            
    results.append(resuts_level)

    return results

r = TreeNode(20, TreeNode(15), TreeNode(7))
root = TreeNode(3, TreeNode(9), r)

#root = None
print(level_order(root))
print(zig_zag(root))