# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 11:18:50 2016

@author: Mike
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1
        ans = [-1, -1]
        while l < r:
            mid = (l + r) / 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if (nums[l] != target):
            return ans
        else:
            ans[0] = l
        
        r = len(nums) -1
        while l < r:
            mid = (l + r) / 2 + 1
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        ans[1] = r
        return ans
        
sln = Solution()
print sln.searchRange([1,1,1,3,3,4,5], 3)        