# -*- coding: utf-8 -*-
"""
Created on Fri Oct 09 17:41:28 2015

@author: Mike
"""

class Solution(object):
    def maxArea(self, height):
        ans, l ,r = 0, 0, len(height) -1
        while l < r:
            ans = max(ans, min(height[r], height[l]) * (r - l))
            if height[r] > height[l]:
                cur = l
                l += 1
                while l < r and height[l] < height[cur]:
                    l += 1
            else:
                cur = r
                r -= 1
                while l < r and height[r] < height[cur]:
                    r -= 1
        return ans
        
sln = Solution()
print sln.maxArea([1,2,9,9,1])