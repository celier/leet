﻿"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        return zip(nums1, nums2)