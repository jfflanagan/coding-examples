def recursive(seq1, seq2, m, n):
    if n < 0 or m < 0:
        return 0
    
    if seq1[m] == seq2[n]:
        return 1 + recursive(seq1, seq2, m - 1, n - 1)
    
    return max(
        recursive(seq1, seq2, m, n - 1),
        recursive(seq1, seq2, m - 1, n)
    )

def dp(seq1, seq2, m, n):
    table = [[0]*(n + 1) for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match_value = 0
            if seq1[i - 1] == seq2[j - 1]:
                match_value = 1
            
            table[i][j] = match_value + max(
                table[i - 1][j - 1],
                table[i - 1][j],
                table[i][j - 1]
                )
            
    print(table)
    return table[m][n]

string1 = "abcde"
string2 = "ace"

#print(recursive(string1, string2, len(string1) - 1, len(string2) - 1))
print(dp(string1, string2, len(string1), len(string2)))

