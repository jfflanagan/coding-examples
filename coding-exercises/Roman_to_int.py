def get_value(c):
    if c == 'M':
        return 1000
    if c == 'D':
        return 500
    if c == 'C':
        return 100
    if c == 'L':
        return 50
    if c == 'X':
        return 10
    if c == 'V':
        return 5
    if c == 'I':
        return 1

def romanToInt(s):
    int_value = 0
    for c in s:
        v = get_value(c)
        int_value += v - 2 * int_value % v

    return int_value

if __name__ == '__main__':
    print(romanToInt("MMXIX"))
