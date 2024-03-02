class Solution:
    def longestCommonPrefix(self, strs):
        longest_prefix = ""
        
        if not strs:
            return longest_prefix

        index = 0
        while index < len(strs[0]):
            first_char = strs[0][index]
            for word in strs[1:]:
                current_char = ""
                if index < len(word): 
                    current_char = word[index]

                if current_char != first_char:
                    return longest_prefix
                first_char = current_char
            
            longest_prefix += first_char
            index += 1
                                    
        return longest_prefix

s = Solution()
strs = ["dog", "dogman", "dogdodo"]
print(s.longestCommonPrefix(strs))