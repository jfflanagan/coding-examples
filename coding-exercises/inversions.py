# Uses python3
import sys

def merge(a, b, num_inv):
    size_a = len(a)
    size_b = len(b)
    c = [0] * (size_a + size_b)

    i = 0
    j = 0
    while i < size_a and j < size_b:
        a_elem = a[i]
        b_elem = b[j]
        if a_elem <= b_elem:
            c[i + j] = a_elem
            i += 1
        else:
            c[i + j] = b_elem
            j += 1
            num_inv += (size_a - i)

    while i < size_a:
        c[i +j] = a[i]
        i += 1

    while j < size_b:
        c[i + j] = b[j]
        j += 1

    return c, num_inv


def merge_sort(a, num_inv):
    
    size = len(a)

    if size == 1:
        return a, 0

    mid = size // 2

    left_array, num_inv_left = merge_sort(a[0:mid], num_inv)
    right_array, num_inv_right = merge_sort(a[mid:size], num_inv)

    return merge(left_array, right_array, num_inv_left + num_inv_right)

def get_number_of_inversions_fast(a):
    _, num_inv = merge_sort(a, 0)

    return num_inv

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)

    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    #print(get_number_of_inversions(a, b, 0, len(a)))
    print(get_number_of_inversions_fast(a))
    #print(merge_sort(a, 0))
