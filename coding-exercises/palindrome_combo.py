results = []

def make_combos(word, my_list):
    if not word:
        return

    n = len(word)

    # divide and conquor
    longest = 0
    longest_i = 0
    for i in range(n):
        size = expand(word, i, n) - 1
        if size > longest:
            longest = size
            longest_i = i

    # branch
    for i in range(longest -1,-1,-1):
        palidrome = word[longest_i - i:longest_i + i + 1]
        new_list = my_list[:]
        new_list.append(palidrome)
        results.append(new_list)

        make_combos(word[:longest_i - i], new_list)
        make_combos(word[longest_i + i + 1:], new_list)

    # main
    palidrome = word[longest_i - longest:longest_i + longest + 1]
    my_list.append(palidrome)
    make_combos(word[:longest_i - longest], my_list)
    make_combos(word[longest_i + longest + 1:], my_list)

def expand(word, i, n):
    size = 0

    left = i
    right = i
    while left >=0 and right < n and word[left] == word[right]:
        left -= 1
        right += 1
        size += 1

    return size


s = "xxxaaab"

my_list = []
results.append(my_list)
make_combos(s, my_list)
print(results)