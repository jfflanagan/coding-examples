
def explore(a, i, j, total):
    if a[i,j] == 0:
        return total

    a[i,j] = 0
    total += 1

    explore(a , i + 1, j, total)
    explore(a , i - 1, j, total)
    explore(a , i, j + 1, total)
    explore(a , i, j - 1, total)

def find_islands(a):
    x,y = a.shape

    islands = []
    for i in range(x):
        for j in range(y):
            area = explore(a, i, j, 0)
            if area:
                islands.append(area)

    return islands
            
                
