import math

def binary_search(my_list, low, high, value):
    
    if low > high:
        # need to check that these indices are valid
        if math.fabs(my_list[low] - value) < math.fabs(my_list[high] - value):
            return my_list[low]
        else:
            return my_list[high]

    mid = low + (high - low) / 2

    if my_list[mid] == value:
        return value

    if value < my_list[mid]:
        return binary_search(my_list, low, mid - 1, value)
    else:
        return binary_search(my_list, mid + 1, high, value)

    return None

my_list = [1, 2, 4,7,7,8,9,10,15]

print(binary_search(my_list, 0, len(my_list) - 1, 6))