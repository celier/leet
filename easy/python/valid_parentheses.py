"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

"""
class Solution:
    def isValid(self, s: str) -> bool:
        dico = {}
        for i, v in enumerate(list(s)):
            if dico[v]:
                dico[v] += 1
            else:
                dico[v] = 0
        res = True
        for key, value in dico.items():
            if value % 2 != 0:
                res = False
                
        return res