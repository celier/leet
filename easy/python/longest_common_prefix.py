"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        else:               
            for index, value in enumerate(list(strs[0])):
                if strs[1][index] != value:
                    return strs[0][0:index - 1]
                
                offset = 0
                t = set()
                for word in strs:
                    size_t = len(t)
                    t.update(list(word))
                    offset = len(t) - size_t
                return strs[0][:offset]