
import copy

def anagrams(word, anagram_list, anagram_stack):
    if not word:
        anagram_list.append(copy.deepcopy(anagram_stack))
        return

    for i, c in enumerate(word):
        anagram_stack.append(c)
        
        sub_word = [sc for j, sc in enumerate(word) if j != i]
        anagrams(sub_word, anagram_list, anagram_stack)

        anagram_stack.pop()


word = ['a', 'b', 'c']

my_list = []
anagrams(word, my_list, [])

print my_list
