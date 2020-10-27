"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
class Solution:
    def reverse(self, x: int) -> int:
        sign = (x > 0)  - (x < 0)
        rev = int(str( x * sign)[::-1])
        return sign * rev * (rev < 2**31)