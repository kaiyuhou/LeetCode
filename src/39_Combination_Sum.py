# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:20:55 2016

@author: Mike
"""

class Solution(object):
    
    def combinationSum(self, candidates, target):
        #s = time.clock()
        ans = []
        candidates.sort();
        self.search(candidates, [], target, ans)
        #print time.clock() - s
        return ans
        
    def search(self, nums, sel, t, ans):
       for i in xrange(len(nums)) :
           if nums[i] > t:
               return
           elif nums[i] == t:
               ans.append(sel + [nums[i]])
               return
           else:
               self.search(nums[i:], sel + [nums[i]], t - nums[i], ans)
               
    
           
sln = Solution()
print sln.combinationSum([20,21,43,47,49,38,40,31,46,35,37,23,25,30,39,22,41,27,42,26,24,45,48,44,33,32], 69)
            
            
            
    
    