def binary_search(matrix, l, r, cols, target):
    if r < l:
        return False

    mid = l + (r - l) // 2

    mid_row = mid // cols
    mid_col = mid % cols

    if matrix[mid_row][mid_col] == target:
        return True

    if target < matrix[mid_row][mid_col]:
        return binary_search(matrix, l, mid - 1, cols, target)
    else:
        return binary_search(matrix, mid + 1, r, cols, target)

def search_matrix(matrix, target):
    if not matrix:
        return False

    row = len(matrix)
    col = len(matrix[0])

    return binary_search(matrix, 0, row*col - 1, col, target)

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
#matrix = [[1, 1]]
print(search_matrix(matrix, 3))


