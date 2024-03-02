def max_multiple(arr):
    n = len(arr)
    
    if n < 3:
        return [-1] * n

    heap = sorted(arr[:3])

    results = [-1] * 2
    results.append(heap[0] * heap[1] * heap[2])
    for i in range(3, n):
        # heap operation to keep track of min
        if arr[i] > heap[0]:
            # extract
            heap[0] = arr[i]

            # shift downs
            swap_index = 1
            if heap[1] > heap[2]:
                swap_index = 2
            
            if heap[0] > heap[swap_index]:
                #swap
                temp = heap[0]
                heap[0] = heap[swap_index]
                heap[swap_index] = temp

        results.append(heap[0] * heap[1] * heap[2])

    return results


print(max_multiple([2, 1, 2, 1, 2]))

        

