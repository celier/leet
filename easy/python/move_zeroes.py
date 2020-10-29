"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) <= 1:
            return 0
        
        newTail = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[index], nums[newTail] = nums[newTail], nums[index]
                newTail += 1
                
        # As a oneliner, but not valid because it's not in place
        # nums.sort(key=bool, reverse=True)