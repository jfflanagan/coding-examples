# Uses python3
def edit_distance(s, t):
    n = len(s)
    m = len(t)
    dp_table = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(0, n + 1):
        dp_table[i][0] = i

    for j in range(0, m + 1):
        dp_table[0][j] = j

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            insertion = dp_table[i][j - 1] + 1
            deletion = dp_table[i - 1][j] + 1
            match = dp_table[i - 1][j - 1]
            mismatch = dp_table[i - 1][j - 1] + 1

            if s[i - 1] == t[j - 1]:
                dp_table[i][j] = min(insertion, deletion, match)
            else:
                dp_table[i][j] = min(insertion, deletion, mismatch)



    return dp_table[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
