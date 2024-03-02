# Uses python3
import sys
from collections import namedtuple

Point = namedtuple('Point', 'index, type, key')

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def swap_points(linesweep):
    # First pass put the start points at the begining in the case two or more point are equal
    j = 0
    for i in range(0, len(linesweep)):
        if linesweep[i].index != linesweep[j].index:
            j = i
        else:
            if linesweep[i].type == 1:
                swap(linesweep, i, j)
                j += 1

    # Second pass put the end points at the end in the case two or more point are equal
    j = len(linesweep) - 1
    for i in range(len(linesweep) -1, -1, -1):
        if linesweep[i].index != linesweep[j].index:
            j = i
        else:
            if linesweep[i].type == 2:
                swap(linesweep, i, j)
                j -= 1


def fast_count_segments(starts, ends, points):
    cnt = [0]*len(points)

    linesweep = []
    for point in starts:
        linesweep.append(Point(index = point, type=1, key=None))

    for point in ends:
        linesweep.append(Point(index = point, type=2, key=None))

    for i, point in enumerate(points):
        linesweep.append(Point(index = point, type=0, key=i))

    linesweep.sort(key=lambda x: x.index)
    swap_points(linesweep)

    intersection_counter = 0
    for point in linesweep:
        if point.type == 0:
            cnt[point.key] = intersection_counter
        if point.type == 1:
            intersection_counter += 1
        if point.type == 2:
            intersection_counter -= 1

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
