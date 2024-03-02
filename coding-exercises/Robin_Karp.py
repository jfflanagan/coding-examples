# python3
class RabinKarp(object):
    def __init__(self):
        self._multiplier = 263
        self._prime = 1000000007

    def _poly_hash(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans

    def precompute_hashes(self, text, pattern_len):
        text_len = len(text)

        h = [0] * (text_len - pattern_len + 1)
        s = text[text_len - pattern_len:text_len]
        h[text_len - pattern_len] = self._poly_hash(s)
        y = 1
        for i in range(1, pattern_len + 1):
            y = (y * self._multiplier) % self._prime
        for i in range(text_len - pattern_len - 1, -1, -1):
            h[i] = ( self._multiplier * h[i+1] + ord(text[i]) - y*ord(text[i + pattern_len]) ) % self._prime

        return h

    def find_pattern(self, pattern, text):
        results= []
        p_hash = self._poly_hash(pattern)
        p_length = len(pattern)
        h = self.precompute_hashes(text, p_length)
        for i in range(len(text) - p_length + 1):
            if p_hash != h[i]:
                continue
            else:
                if text[i:i+p_length] == pattern:
                    results.append(i)

        return results
        
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences_fast(pattern, text):
    rc = RabinKarp()
    return rc.find_pattern(pattern, text)

def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

if __name__ == '__main__':
    print_occurrences(get_occurrences_fast(*read_input()))

