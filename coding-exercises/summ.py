# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.summ = 0
        
    def traverse(self, root, num_stack):
        if root is None:
            return
        
        num_stack.append(root.val)
        
        # leaf
        if root.right is None and root.left is None:
            m = 1
            number = 0
            for i in range(len(num_stack)-1,-1,-1):
                number += num_stack[i]*m
                m *= 10
            self.summ += number
            
        self.traverse(root.left, num_stack)
        
        self.traverse(root.right, num_stack)

        num_stack.pop()
        
        
    def sumNumbers(self, root):
        self.traverse(root, [])
        
        return self.summ

root = TreeNode(1, TreeNode(2), TreeNode(3))
s = Solution()
s.sumNumbers(root)