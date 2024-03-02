
count = []
class Solution:
    def __init__(self):
        self.count = 0

    def find_paths(self, m, n, i, j, matrix):
        if i == m - 1 and j == n - 1:
            self.count += 1
            return

        if matrix[i][j] == 1:
            return

        matrix[i][j] = 1

        if i < m - 1:
            self.find_paths(m, n, i + 1, j, matrix)

        if j < n - 1:
            self.find_paths(m, n, i, j + 1, matrix)

        # Back track
        matrix[i][j] = 0

    def unique_paths(self, m, n):
        matrix = [[0]*n for i in range(m)]
        self.find_paths(m, n, 0, 0, matrix)

s = Solution()
s.unique_paths(3, 3)
print(s.count)

