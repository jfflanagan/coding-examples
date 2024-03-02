def are_sides_equal(arr):
    if len(arr) < 2:
        return False

    arr.sort()

    i = 0
    j = len(arr) - 1
    sum_left = arr[i]
    sum_right = arr[j]
    while i < j - 1:
        if sum_left <= sum_right:
            i += 1
            sum_left += arr[i]
        else:
            j -= 1
            sum_right += arr[j]

    return sum_left == sum_right and arr[i] < arr[j]


#arr = [1, 5, 7, 1] # true
#arr = [2, 1, 2, 5] # true
#arr = [3, 6, 3, 4, 4] # false
#arr =  [12, 7, 6, 7, 6] #false
print(are_sides_equal(arr))

