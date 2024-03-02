l = [7,2,1,6,8,5,3,4]

def swap(my_list, first, second):
    temp = my_list[first]
    my_list[first] = my_list[second]
    my_list[second] = temp

def partition(my_list, start, end):
    pivot = my_list[end] # right most element
    pivot_index = start
    for i in range(start, end):
        if my_list[i] <= pivot:
            swap(my_list, i, pivot_index)
            pivot_index += 1
    swap(my_list, pivot_index, end)

    return pivot_index        

def quick_sort(my_mist, start, end):
    if start >= end: return

    pivot_index = partition(my_mist, start, end)

    quick_sort(my_mist, start, pivot_index - 1)
    quick_sort(my_mist, pivot_index + 1, end)

quick_sort(l, 0, len(l) - 1)

print(l)