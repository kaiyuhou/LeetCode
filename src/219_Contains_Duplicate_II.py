# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:45:17 2015

@author: Mike
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pos = {}
        for i,v in enumerate(nums):
            if v in pos and i - pos[v] <= k:
                return True
            pos[v] = i
        return False
        
sln = Solution()
print sln.containsNearbyDuplicate([1,2,1],2)