"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, 
write a function to search target in nums.
If target exists, then return its index, otherwise return -1.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or target == '' or target not in nums:
            return -1
        
        mid = round(len(nums) / 2)
        search_start = 0
        search_end = len(nums) - 1
        
        while True:
            if target == nums[mid]:
                return mid
            else:
                if target > nums[mid]:
                    search_start = mid + 1
                    mid = search_start + (search_end - search_start)
                else:
                    search_end = mid - 1
                    mid = search_start + (search_end - search_start)