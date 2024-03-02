res = []

def dfs(start, s, n, path):
    if start == n:
        res.append(path.copy())
        return

    for end in range(start + 1, n + 1):
        substr = s[start: end]
        if substr == substr[::-1]:
            path.append(substr)
            dfs(end, s, n, path)
            path.pop()

def partition(s):
    n = len(s)

    dfs(0, s, n, [])
    return res

print(partition("abaa"))