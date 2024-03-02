class Node(object):
    def __init__(self, next, previous, value):
        self.next = next
        self.previous = previous
        self.value = value

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add_node(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
            
    def delete(self, node):
        previous_node = node.previous
        if previous_node is not None:
            previous_node.next = node.next

        next_node = node.next
        if node.next is not None:
            next_node.previous = previous_node

    def insert_item(self, node, insertion_node):
        previous_node = insertion_node.previous
        if previous_node is not None:
           previous_node.next = node
        node.previous = previous_node

        insertion_node.previous = node
        node.next = insertion_node
         

b_item = Node(None, None, 'b')
c_item = Node(None, None, 'c')

ll = LinkedList()
ll.add_node(Node(None, None, 'a'))
ll.add_node(b_item)
ll.add_node(c_item)
ll.add_node(Node(None, None, 'd'))

ll.delete(b_item)
ll.insert_item(Node(None, None, 'z'), c_item)

item = ll.head
while item is not None:
    print(item.value)
    item = item.next 
