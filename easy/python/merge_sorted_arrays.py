"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        available_space = len(nums1) - len(nums2)
         # Insert values first
        for i in range(len(nums2)):
            if nums1[available_space + i] == 0:
                nums1[available_space + i] = nums2[i]
        
        # Then sort the array
        nums1.sort()
        