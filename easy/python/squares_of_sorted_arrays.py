"""
Given an array of integers A sorted in non-decreasing order, 
return an array of the squares of each number, also in sorted non-decreasing order.
Example:
    Input:  [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
"""
import collections
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if len(A) <= 1:
            A[0] = A[0] ** 2
            return A
        # Not a valid answer considering requirements
        return sorted([value ** 2 for value in A])
    
    # Solution with a queue
    def sortedSquaresDeque(self, A):
        answer = collections.deque()
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1
        return list(answer)
    
    # Solution without import 
    def sortedSquaresBest(self, A):
        answer = [0] * len(A)
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer[r - l] = left * left
                l += 1
            else:
                answer[r - l] = right * right
                r -= 1
        return answer