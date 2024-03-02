# Uses python3
import sys
import random

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def partition3(a, l, r):
    x = a[l]
    j = l
    k = 0
    for i in range(l + 1, r + 1):
        # first classical partition move
        if a[i] <= x:
            j += 1
            swap(a, i, j)
        # Then move to the x < p range if needed
        if a[j] < x:
            swap(a, j, j - k)
        # increment p range if needed
        if a[j] == 0:
            k += 1

    swap(a, l, j - k)

    return j - k, j


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            swap(a, i, j)
    swap(a, l, j)

    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    swap(a, l, k)

    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
