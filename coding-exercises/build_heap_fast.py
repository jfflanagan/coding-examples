# python3

def sift_down(data, n, index, swaps):
    min_index = index
    left_child = 2 * index + 1
    if left_child < n and data[left_child] < data[min_index]:
        min_index = left_child

    right_child = 2 * index + 2
    if right_child < n and data[right_child] < data[min_index]:
        min_index = right_child

    if min_index != index:
        swaps.append((index, min_index))

        temp = data[index]
        data[index] = data[min_index]
        data[min_index] = temp

        sift_down(data, n, min_index, swaps)

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    n = len(data)

    swaps = []
    i = n // 2 - 1
    while i >= 0:
        sift_down(data, n, i, swaps)
        i-= 1

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
    #swaps = build_heap([5, 4, 3, 2, 1])

    #print(len(swaps))
    #for i, j in swaps:
    #    print(i, j)