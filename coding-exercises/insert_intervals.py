
def find_nearest_start(intervals, l, r, target):
    if r < l:
        if l >= len(intervals):
            return len(intervals) - 1

        if r < 0:
            return 0

        if (target - intervals[r][0]) < (intervals[l][0] - target):
            return r
        else:
            return l

    mid = l + (r -l) // 2

    if intervals[mid][0] == target:
        return mid

    if target < intervals[mid][0]:
        return find_nearest_start(intervals, l, mid - 1, target)
    else:
        return find_nearest_start(intervals, mid + 1, r, target)
    
print(find_nearest_start([[1],[2],[6],[7],[8]], 0, 4, 5))
#def insert_intervals():
