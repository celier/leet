"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
"""
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # Divide and conquer
        even = []
        odd = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd
    
        # In-place solution
        # i = 0
        # j = len(A)-1
        
        # while i < j:
        #     if A[i] % 2 > A[j] % 2:
        #         A[i], A[j] = A[j], A[i]
        #     if A[i] % 2 == 0: i += 1
        #     if A[j] % 2 == 1: j -= 1
        # return A