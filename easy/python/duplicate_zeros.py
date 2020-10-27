"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.
"""
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        offset = 0
        for i, v in enumerate(list(arr)):
            if v == 0:
                print(i)
                arr.insert(i + offset, 0)
                offset += 1
                del arr[len(arr) - 1]