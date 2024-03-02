word_list = ['cat', 'act', 'mine', 'nime', 'mien' ]

anagram_list = {}
for word in word_list:
    key = list(word)
    key.sort()
    str_key = ""
    for c in key:
        str_key += c

    if str_key not in anagram_list:
        anagram_list[str_key] = []
    anagram_list[str_key].append(word)

print(anagram_list)