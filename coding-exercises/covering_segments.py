# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []

    segments.sort(key=lambda x: x.start)

    safe_point = -1
    for segment in segments:
        if segment.start <= safe_point:
            safe_point = min(safe_point, segment.end)
            points[-1] = safe_point
        else:
            safe_point = segment.end
            points.append(safe_point)

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
