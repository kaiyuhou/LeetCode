# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:31:29 2015

@author: Mike
"""

class Solution(object):
    def removeDuplicates(self, nums):
        if nums == []:
            return 0          
        i = 1
        p = 1
        while i < len(nums):
            if nums[i] > nums[i-1]:
                nums[p] = nums[i]
                p += 1
            i += 1
        return p
        
sln = Solution()
print sln.removeDuplicates([1,1,2,2,3,3,4,5,6,6,6])