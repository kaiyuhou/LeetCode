# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 14:55:41 2016

@author: Mike
"""

class Solution(object):
    def nextper(self, nums, ans, sel, v):
        if len(sel) == len(nums):
            ans.append(sel)
            return            
        for i in range(len(nums)):
            if v[i]:
                continue
            v[i] = 1
            self.nextper(nums, ans, sel + [nums[i]], v)
            v[i] = 0
   
    def permute(self, nums):
        ans = []
        v = [0 for i in range(len(nums))]
        self.nextper(nums,ans,[], v)
        return ans
        
sln = Solution()
print sln.permute([1,2,3])
        