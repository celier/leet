"""
Given a roman numeral, convert it to an integer.
"""
class Solution:
    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        year = 0
        for index in range(0, len(s) - 1):
            if roman[s[index]] < roman[s[index+1]]:
                year -= roman[s[index]]
            else:
                year += roman[s[index]]
        return year + roman[s[-1]]