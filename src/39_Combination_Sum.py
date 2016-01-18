# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:20:55 2016

@author: Mike
"""

class Solution(object):
    ans = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.search(candidates,[], target)
        return self.ans
        
    def search(self, nums, sel, t):
        if t == 0:
            self.ans.append(sel)
            return 
        
        if nums == []:
            return 
        
        if nums[-1] > t:
            self.search(nums[:-1], t)
        
        for i in range(len(nums[])
            
            
    
    