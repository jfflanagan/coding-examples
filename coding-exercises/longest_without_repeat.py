def lengthOfLongestSubstring(s):
    lastIndex = [-1] * 256


    start_index = 0
    longest = 0
    for i, c in enumerate(s):
        start_index = max(start_index, lastIndex[ord(c)] + 1)

        longest = max(longest, i - start_index + 1)
        lastIndex[ord(c)] = i

    return longest

if __name__ == '__main__':
    print(lengthOfLongestSubstring("GEEKSFORGEEKS"))

    