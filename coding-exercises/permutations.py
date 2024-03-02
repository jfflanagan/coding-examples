def merge_intervals(intervals):
    if not intervals:
        return [[]]

    merged_intervals = []
    intervals.sort(key=lambda x: x[0])

    current_interval = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] > current_interval[1]:
            merged_intervals.append(current_interval)
            current_interval = intervals[i]
        else:
            current_interval[1] = max(current_interval[1], intervals[i][1])

    merged_intervals.append(current_interval)

    return merged_intervals



    





#print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
print(merge_intervals([[1,4],[2,3]]))