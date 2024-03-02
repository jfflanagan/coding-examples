class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_duplicates(head):
    # dummy takes care of beggining issues
    dummy = ListNode(float('-inf'))
    dummy.next = head

    p = dummy
    j = dummy
    current = head
    while current != None:
        if current.next is not None:
            # middle
            if p.val < current.val and current.next.val > current.val:
                j.next = current
                j = current
        else:
            # end
            if current.next is None:
                if p.val < current.val:
                    j.next = current
                    j = current
                else:
                    j.next = None 

        p = current
        current = current.next

    return dummy.next

head = ListNode(1)
n2 = ListNode(2)
head.next = n2
n3 = ListNode(3)
n2.next = n3
n4 = ListNode(3)
n3.next = n4
n5 = ListNode(4)
n4.next = n5
n6 = ListNode(6)
n5.next = n6
n7 = ListNode(6)
n6.next = n7 

head = remove_duplicates(head)

