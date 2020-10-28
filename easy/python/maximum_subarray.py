"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
    
After finding a solution, check https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = 0
        current_sum = 0
        for x in nums:
            current_sum = max(0, current_sum + x)
            best_sum = max(best_sum, current_sum)
        return best_sum