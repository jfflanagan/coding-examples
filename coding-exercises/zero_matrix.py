def zero_matrix(matrix):
    r = len(matrix)
    c = len(matrix[0])

    zero_row = False
    for i in range(r):
        if not matrix[i][0]:
            zero_row = True
            break

    zero_col = False
    for j in range(c):
        if not matrix[0][j]:
            zero_col = True
            break

    for i in range(r):
        for j in range(c):
            if not matrix[i][j]:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, r):
        if not matrix[i][0]:
            for j in  range(c):
                matrix[i][j] = 0

    for j in range(1, c):
        if not matrix[0][j]:
            for i in  range(r):
                matrix[i][j] = 0 

    if zero_row:
        for i in range(r):
            matrix[i][0] = 0

    if zero_col:
        for j in range(c):
            matrix[0][j] = 0  

    return matrix

#matrix = [[1,2,3],[4,0,6],[7,8,9]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

print(zero_matrix(matrix))
