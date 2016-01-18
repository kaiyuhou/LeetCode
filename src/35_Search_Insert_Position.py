# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 09:59:46 2016

@author: Mike
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0,len(nums) -1
        while l < r:
            m = (l + r)/2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l if nums[l] >= target else l + 1
        
sln = Solution()
print sln.searchInsert([1,3,5,6], 0)