def merge(left, right, target_array):
    len_left = len(left)
    len_right = len(right)

    i = 0
    j = 0
    k = 0
    inversions = 0
    while(i < len_left and j < len_right):
        if left[i] <= right[j]:
            target_array[k] = left[i]
            i += 1
            inversions += j
        else:
            target_array[k] = right[j]
            j += 1
        k += 1

    while i < len_left:
        target_array[k] = left[i]
        k += 1
        i += 1
        inversions += j

    while j < len_right:
        target_array[k] = right[j]
        k += 1
        j += 1

    return inversions


def merge_sort(my_list):
    n = len(my_list)

    if n < 2:
        return 0

    mid = n / 2
    left = [my_list[i] for i in range(0, mid)]
    right = [my_list[j] for j in range(mid, n)]

    left_inversions = merge_sort(left)
    right_inversions = merge_sort(right)
    return merge(left, right, my_list) + left_inversions + right_inversions

def incrStack(arr):
    num_swaps = 0
    for i in range(1, len(arr)):
        for j  in range(1, len(arr) - i + 1):
            if arr[j] < arr[j - 1]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp
                num_swaps += 1
    print(num_swaps)

def incrStack2(arr):
    num_swaps = merge_sort(arr)

    print(num_swaps)

l = [10,14,8,49,9,1,9,3]
ll = [i for i in l]

incrStack(l)

incrStack2(ll)

print(ll)