# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 09:51:58 2016

@author: Mike
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2 :
            return 
        i = len(nums) - 1;
        while i > 0:
            if nums[i -1] < nums[i]:
                break
            i -= 1
        if i == 0:  # all nums a increaseing
            nums.reverse()
            return
        i -= 1
        for j in range(len(nums)-1, i, -1):
            if nums[j] > nums[i]:
                break
        nums[i],nums[j] = nums[j],nums[i]
        nums[i + 1:] = nums[:i:-1]
        
        #print nums

sln = Solution()
print sln.nextPermutation([1,3,2,4])
            
            
            