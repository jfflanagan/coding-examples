class Node:
    def __init__(self, next, value, idx):
        self.next = next
        self.value = value
        self.idx = idx


def queue_game(arr, x):
    results = []
    if not arr:
        return results

    # initialize queue
    head = Node(None, arr[0], 1)
    current = head
    for i in range(1, len(arr)):
        current.next = Node(None, arr[i], i + 1)
        current = current.next
    tail = current

    # perfrom x iterations of the rules
    for it in range(x):
        # rule #1 dequeue x items max end of queue and record the first max
        node_list = []
        max_node = None
        for i in range(x):
            if not max_node or max_node.value < head.value:
                max_node = head
            node_list.append(head)
            head = head.next

            if head is None:
                tail = None
                break

        # record the index of the excluded item
        if max_node:
            results.append(max_node.idx)

        # enqueue the included items
        for node in node_list:
            if node.idx == max_node.idx:
                continue
            node.value = max(0, node.value - 1)
            if not tail:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node
                tail.next = None

    return results
        
x = 5
arr = [1,2,2,3,4,5]
x=4
arr = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]

print(queue_game(arr, x))