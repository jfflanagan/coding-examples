from queue import Queue

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_map = [{} for i in range(len(wordList[0]))]
        words = set(wordList)
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        q = Queue()
        q.put((1, beginWord))

        while not q.empty():
            level, word = q.get()
        
            for i in range(len(word)):
                for c in alphabet:
                    new_word = word[:i] + c + word[i+1:]

                    if new_word in words:
                        if new_word == endWord:
                            return level + 1
                        # put in queue
                        q.put((level + 1, new_word))

                        words.remove(new_word)

        return 0

s = Solution()
words = ["hot","dot","dog","lot","log"]
r = s.ladderLength("hit", "cog", words)
print(r)



