"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]
"""
import collections
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return False
        
        s = collections.Counter(arr)
    
        #check if there are more than one zeros
        if(s[0]>1):
            return True

        for num in arr:
            if s[2*num] and num!=0:
                return True
        return False