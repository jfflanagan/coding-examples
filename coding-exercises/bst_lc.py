class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pre_order(root):
    stack = []
    results = []

    while True:
        while root is not None:
            results.append(root.val)

            stack.append(root)
            root = root.left

        if not stack:
            return results

        root = stack.pop()
        root = root.right


root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(pre_order(root))