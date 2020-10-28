"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        newTail = 0
        
        for index in range(1, len(nums)):
            if nums[index] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[index]
        
        return newTail + 1