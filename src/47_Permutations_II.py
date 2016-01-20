# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:20:04 2016

@author: Mike
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #nums.sort()
        ans = [[]]
        for i in nums:
            cur = []
            for j in ans:
                for k in range(len(j) + 1):
                    cur.append(j[:k] + [i] + j[k:])
                    if k < len(j) and j[k] == i:
                        break
            ans = cur
        return ans
        
        
        
sln = Solution()
print sln.permuteUnique([1,1,3])
        