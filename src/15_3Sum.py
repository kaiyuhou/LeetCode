# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:39:11 2015

@author: Mike
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l = 0
        r = len(nums) - 1
        ans = []
        while nums[l] < 0 and nums[r] > 0:
            if nums[r] > -nums[l]:
                if nums[r] + nums[l] > nums[l]:
                    r -= 1
                else:
                    if -(nums[r] + nums[l]) in nums[r+1:l]:
                        ans.append([nums[l],-(nums[r] + nums[l]),nums[r]])