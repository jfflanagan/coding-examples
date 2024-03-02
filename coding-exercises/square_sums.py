
def square_sums(square, ri, ci, rf, cf):
    # assume square or rectangluar list of lists
    n = len(square)
    m = len(square[1])
    row_sums = []

    for i in range(n):
        row_sum = [square[i][0]]
        for j in range(1, m):
            row_sum.append(row_sum[-1] + square[i][j])

        row_sums.append(row_sum)

    square_sums = []
    for j in range(m):
        square_sum = [row_sums[0][j]]
        for i in range(1, n):
            square_sum.append(square_sum[-1] + row_sums[i][j])

        square_sums.append(square_sum)

    # square_sums is transposed
    result = square_sums[cf][rf]
    if ri > 0:
        result -= square_sums[cf][ri - 1]
    if ci > 0:
        result -= square_sums[ci - 1] [rf]
    if ri > 0 and ci > 0:
        result += square_sums[ci - 1][ri - 1]

    return result





a = [[1,2,3], [4,5,6], [7,8,9]]
print(square_sums(a, 1, 0, 2, 1))