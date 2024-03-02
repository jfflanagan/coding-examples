def longest_o_n(text):
    padded_text = "$"
    for c in text:
        padded_text += c + "$"

    palindrone_arrray = [0] * len(padded_text)

    mirror_line = 0
    right_border = 0
    max_palindrome = 0
    index_palindrome = -1

    for i in range(len(padded_text)):
        mirror_i = mirror_line - (i - mirror_line)

        if i < right_border:
            palindrone_arrray[i] = min(palindrone_arrray[mirror_i], right_border - i)

        if palindrone_arrray[i] + i >= right_border:
            while i - 1 - palindrone_arrray[i] >= 0 and i + 1 + palindrone_arrray[i] < len(palindrone_arrray) and padded_text[i - 1 - palindrone_arrray[i]] == padded_text[i + 1 + palindrone_arrray[i]]:
            
                palindrone_arrray[i] += 1

        if (i + palindrone_arrray[i]) > right_border:
            mirror_line = i
            right_border = i + palindrone_arrray[i]

        if palindrone_arrray[i] > max_palindrome:
            max_palindrome = palindrone_arrray[i]
            index_palindrome = i

    if index_palindrome % 2:
        return text[(index_palindrome -1) // 2 -  (max_palindrome - 1) // 2: (index_palindrome -1) // 2 + (max_palindrome + 1) // 2]
    else:
        return text[index_palindrome // 2 - max_palindrome // 2 :index_palindrome // 2 + max_palindrome // 2]



def longest_o_n_sqr(text):
    longest_palindrome = 1
    for i in range(len(text)):
        test_palindrome = 2 * expand(text, i, i) - 1

        longest_palindrome = max(longest_palindrome, test_palindrome) 

        test_palindrome = 2 * expand(text, i, i + 1)

        longest_palindrome = max(longest_palindrome, test_palindrome)

    return longest_palindrome


def expand(text, start, end):
    i = 0
    while (start - i) >= 0 and (end + i) < len(text):
        if text[start - i] != text[end + i]:
            break
        i += 1

    return i

if __name__ == '__main__':
    #print(longest_o_n("forgeeksskeegfor"))
    print(longest_o_n("babad"))
    #print(longest_o_n("abaabc"))