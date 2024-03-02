# Uses python3
import sys

def gcd_fast(a, b):
    x = max(a, b)
    y = min(a, b)

    if y == 0:
        return x

    xp = x % y

    return gcd_fast(y, xp)

def lcm_fast(a, b):
    x = max(a, b)
    y = min(a, b)

    return (x // gcd_fast(x, y)) * y

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

#a, b = map(int, input().split())
#print(lcm_fast(a, b))
if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

