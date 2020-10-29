"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1.

After doing so, return the array.
"""
class Solution:
    # Execution time around 4500 ms
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) < 1:
            return False
        
        for i in range(0, len(arr) - 1):
            arr[i] = max(arr[i + 1:])
        
        arr[-1] = -1
        return arr
    
    # Execution time around 120 ms
    # def replaceElements(self, arr: List[int]) -> List[int]:
    #    max_val = -1
    #    max_index = 0
    #    
    #    for index in range(len(arr) - 1):
    #        if max_val == -1 or arr[index] == max_val:
    #            max_val = max(arr[(index + 1):])
    #        arr[index] = max_val       
    #    arr[-1] = -1
    #    return arr