class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    my_stack = []

    # step 1 fill the stack
    current = head
    while current is not None:
        my_stack.append(current)
        current = current.next


    # step 2 reorder
    current = head
    while current is not None and my_stack:
        last_node = my_stack.pop()

        if current == last_node:
            last_node.next = None
            break

        if last_node.next is not None and current == last_node.next:
            last_node.next.next = None
            break

        # insert
        temp = current.next
        current.next = last_node
        last_node.next = temp

        current = temp

    return head



#n5 = ListNode(5)
n4 = ListNode(4)
n3 = ListNode(3,n4)
n2 = ListNode(2,n3)
n1 = ListNode(1,n2)

reorder_list(n1)