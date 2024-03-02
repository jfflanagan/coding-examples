# python3
import sys


def compute_min_refills(distance, tank, stops):
    refill = 0 #refilled at start
    num_stops = 0
    last_stop = 0 #last stop was at the start
    stops.append(distance) # must be able to stop at the destination 
    for stop in stops:
        # cannot complete this segment
        if stop - last_stop > tank:
            return -1

        # Cant reach this stop, so refil at the previous stop
        if stop - refill > tank:
            refill = last_stop 
            num_stops += 1
            
        last_stop = stop

    return num_stops

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
