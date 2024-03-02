# python3
import sys

def generate_prefixes(pattern):
    borders = [0]*len(pattern)
    border = 0
    for i in range(1, len(pattern)):
        while border > 0 and pattern[i] != pattern[border]:
            border = borders[border - 1]

        if pattern[i] == pattern[border]:
            border += 1
        else:
            border = 0

        borders[i] = border

    return borders

def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    result = []
    concat = pattern + '$' + text
    borders = generate_prefixes(concat)
    pattern_len = len(pattern)
    for i in range(2 * pattern_len, len(concat)):
        if borders[i] == pattern_len:
            result.append(i - 2 * pattern_len)

    # Implement this function yourself
    return result


if __name__ == '__main__':
    #print(find_pattern("abra", "abracadabra"))
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))

