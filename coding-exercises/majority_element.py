# Uses python3
import sys
import math

def count_votes(a, left, right, x):
    count = 0
    for i in range(0, right - left + 1):
        if a[i + left] == x:
            count += 1
    return count
    
def get_majority_element(a, left, right):

    mid = (right - left) // 2 + left

    if right == left:
        return a[left]

    left_majority = get_majority_element(a, left, mid)
    right_majority = get_majority_element(a, mid + 1, right)

    if left_majority == right_majority:
        return left_majority

    k = math.ceil((right - left) / 2)
    
    if left_majority > -1:
        left_counts = count_votes(a, left, right, left_majority)
        if left_counts > k:
            return left_majority

    if right_majority > -1:
        right_counts = count_votes(a, left, right, right_majority)
        if right_counts > k:
            return right_majority

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n - 1) != -1:
        print(1)
    else:
        print(0)
