# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:58:42 2015

@author: Mike
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        i = 0
        while i < len(nums):
            tmp = nums[i]
            while i + 1 < len(nums) and nums[i+1] - nums[i] == 1:
                i += 1
            if tmp != nums[i]:
                ans.append(str(tmp) + '->' + str(nums[i]))
            else:
                ans.append(str(tmp))
            i += 1
        return ans
        
sln = Solution()
print sln.summaryRanges([0,1])
            