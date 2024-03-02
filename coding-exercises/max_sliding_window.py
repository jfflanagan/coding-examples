# python3
from collections import deque

def max_sliding_window(items, k):
    max_numbers = []
    
    if not items:
        return max_numbers

    dq = deque()
    for i in range(0, min(k, len(items))):
        while dq and items[i] > items[dq[-1]]:
            dq.pop()

        dq.append(i)

    max_numbers.append(items[dq[0]])

    for i in range(k, len(items)):
        #remove items from left side that drop outside the window, useless items
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        #remove items from the right side of the queue, that cannot be the max, given a new element coming into view
        while dq and items[i] > items[dq[-1]]:
            dq.pop()

        dq.append(i)

        max_numbers.append(items[dq[0]])

    return max_numbers

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))

