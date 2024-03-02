import math
  
def is_solution(perm, l, n):
    for i in range(0, l):
        if l - i == math.fabs(perm[l] - perm[i]):
            return False

    return True


def permutation(perm, l, n, results):
    if l == n:
        results.append(perm[:])
        return

    for i in range(l, n):
        #swap
        temp = perm[l]
        perm[l] = perm[i]
        perm[i] = temp

        if is_solution(perm, l, n):
            permutation(perm, l + 1, n, results)

        #swap back
        temp = perm[l]
        perm[l] = perm[i]
        perm[i] = temp

    return None

results = []
permutation([0,1,2,3], 0, 4, results)
print(len(results))
        

