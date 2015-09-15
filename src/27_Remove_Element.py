# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 18:48:22 2015

@author: Mike
"""

class Solution(object):
    def removeElement(self, nums, val):
        tail = len(nums)
        i = 0
        while i < tail:
            while tail > 0 and nums[tail -1] == val:
                tail -= 1
            if nums[i] == val and i < tail:
                nums[i] = nums[tail-1]
                tail -= 1
            i += 1
        return tail
        
sln = Solution()
print sln.removeElement([3,3],3)