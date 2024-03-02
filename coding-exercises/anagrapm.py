word_list = ['cat', 'act', 'top', 'pot', 'pto']

anagram_list = {}
for word in word_list:
    key = list(word)
    key = sorted(word)

    string_key = ""
    for c in key:
        string_key += c

    if string_key not in anagram_list:
        anagram_list[string_key] = []

    anagram_list[string_key].append(word)

print anagram_list


    