def find_word(board, visited, word, m, n, i, j, k):
    if visited[i][j]:
        return False

    if board[i][j] != word[k]:
        return False

    if (k == len(word) - 1):
        if board[i][j] == word[k]:
            return True
        else:
            return False

    visited[i][j] = 1
    
    if i < m - 1:
        if find_word(board, visited, word, m, n, i + 1, j, k + 1):
            return True
    if i > 0:
        if find_word(board, visited, word, m, n, i - 1, j, k + 1):
            return True
    if j < n - 1:
        if find_word(board, visited, word, m, n, i, j + 1, k + 1):
            return True
    if j > 0:
        if find_word(board, visited, word, m, n, i, j - 1, k + 1):
            return True

    visited[i][j] = 0

    return False

def word_search(board, word):
    # Correct?
    if not word:
        return True

    m = len(board)
    n = len(board[1])
    visited = [[0]*n for i in range(m)]

    for i in range(m):
        for j in range(n):
            if find_word(board, visited, word, m, n, i, j, 0):
                return True

    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCXED"

print(word_search(board, word))