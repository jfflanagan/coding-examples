def dfs(board, x, y, x_dim, y_dim):
    if x < 0 or x >= x_dim or y < 0 or y >= y_dim:
        return

    if board[y][x] != 'O':
        return

    board[y][x] = 'T'

    dfs(board, x - 1, y, x_dim, y_dim)
    dfs(board, x + 1, y, x_dim, y_dim)
    dfs(board, x, y - 1, x_dim, y_dim)
    dfs(board, x, y + 1, x_dim, y_dim)

def flip(board):
    x_dim = len(board[0])
    y_dim = len(board)

    for x in range(x_dim):
        dfs(board, x, 0, x_dim, y_dim)
        dfs(board, x, y_dim - 1, x_dim, y_dim)

    for y in range(y_dim):
        dfs(board, 0, y, x_dim, y_dim)
        dfs(board, x_dim - 1, y, x_dim, y_dim)

    # remove internal Os
    for x in range(x_dim):
        for y in range(y_dim):
            if board[y][x] == 'O':
                board[y][x] = 'X'

    # set temps to Os
    for x in range(x_dim):
        for y in range(y_dim):
            if board[y][x] == 'T':
                board[y][x] = 'O'

board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']]


flip(board)
print(board)

  

