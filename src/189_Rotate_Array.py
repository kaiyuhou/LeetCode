# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:21:34 2015

@author: Mike
"""
class Solution(object):
    def rotate(self, nums, k):
        k = len(nums) - k % len(nums)
        nums[:] = nums[k:] + nums[:k]
        
sln = Solution()
print sln.rotate([1,2], 1)