class Node:
    def __init__(self, value, left, right):
        self.left = left
        self.right = right
        self.value = value

def find_value(node, target):
    if node is None:
        return None
    
    if node.value == target:
        return target
    
    if target < node.value:
        return find_value(node.left, target)
    else:
        return find_value(node.right, target)
    
def get_values(node, vallist):
    if node is None:
        return
    
    get_values(node.left, vallist)
    vallist.append(node.value)
    get_values(node.right, vallist)



n1 = Node(1, None, None)
n4 = Node(4, None, None)
n7 = Node(7, None, None)
n6 = Node(6, n4, n7)
n3 = Node(3, n1, n6)
n13 = Node(13, None, None)
n14 = Node(14, n13, None)
n10 = Node(10, None, n14)
root = Node(8, n3, n10)

print(find_value(root, 14))

mylist = []
get_values(root, mylist)
print(mylist)

img = cv2.imread("test.tif", 0)

for i in range(1, 1e6):
    count += i