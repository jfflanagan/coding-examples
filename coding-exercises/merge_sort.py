def merge(left, right, target_array):
    len_left = len(left)
    len_right = len(right)

    i = 0
    j = 0
    k = 0
    while(i < len_left and j < len_right):
        if left[i] < right[j]:
            target_array[k] = left[i]
            i += 1
        else:
            target_array[k] = right[j]
            j += 1
        k += 1

    while i < len_left:
        target_array[k] = left[i]
        k += 1
        i += 1

    while j < len_right:
        target_array[k] = right[j]
        k += 1
        j += 1


def merge_sort(my_list):
    n = len(my_list)

    if n < 2:
        return

    mid = n // 2
    right = my_list[0:mid]
    left = my_list[mid:n]

    merge_sort(left)
    merge_sort(right)
    merge(left, right, my_list)

test_list = [2,4,1,6,8,5,3,7, 9]

merge_sort(test_list)
print(test_list)
