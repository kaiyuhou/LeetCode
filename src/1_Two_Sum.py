# -*- coding: utf-8 -*-
"""
Created on Fri Oct 09 10:23:33 2015

@author: Mike
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for (i,v) in enumerate(nums):
            if target - v in d:
                return [d[target-v]+1,i+1]
            d[v] = i
                
        
sln = Solution()
print sln.twoSum([0,3,2,4,0],0)