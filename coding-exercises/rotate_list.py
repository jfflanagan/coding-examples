class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def rotate_list(head, k):
    if not head:
        return head

    # possible to do without the stack but requires two passes
    my_stack = []

    current_node = head
    while current_node is not None:
        my_stack.append(current_node)
        current_node = current_node.next

    n = len(my_stack)

    # head
    idx = (n - k) % n
    head = my_stack[idx]
    #end
    my_stack[-1].next = my_stack[0]
    #new end
    idx_end = (n - k - 1) % n
    my_stack[idx_end].next = None

    return head

#l5 = ListNode(5)
#l4 = ListNode(4)
#l4.next = l5
l3 = ListNode(2)
#l3.next = l4
l2 = ListNode(1)
l2.next = l3
l1 = ListNode(0)
l1.next = l2

head = l1

rotate_list(None, 0)
