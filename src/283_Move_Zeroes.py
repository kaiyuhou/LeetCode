# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:31:45 2015

@author: Mike
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p = 0
        i = 0
        while p < len(nums):
            while p <len(nums)-1 and nums[p] == 0:
                p += 1
            if nums[i] == 0:
                nums[i] = nums[p]
                nums[p] = 0
            i += 1
            p += 1

sln = Solution()
sln.moveZeroes([0,0,0,1])