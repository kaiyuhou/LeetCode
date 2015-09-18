# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:05:03 2015

@author: Mike
"""

"""
your runtime beats 93.93% of python submissions
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i - 1],dp[i - 2] + nums[i])
        return dp[-1]
        
sln = Solution()
print sln.rob([1,2,3,4,5,6])