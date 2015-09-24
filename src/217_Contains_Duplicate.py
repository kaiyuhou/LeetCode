# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:40:37 2015

@author: Mike
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
        
sln = Solution()
print sln.containsDuplicate("aabcde")