# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 09:25:20 2016

@author: Mike
"""

class Solution(object):
    
    def combinationSum2(self, candidates, target):
        ans = []
        candidates.sort();
        self.search(candidates, [], target, ans)
#        i = 0        
#        while i < len(ans) -1:
#            if ans[i] == ans [i+1]:
#                ans.remove(ans[i])
#            else:
#                i += 1
        return ans
        
    def search(self, nums, sel, t, ans):
       for i in xrange(len(nums)) :
           if nums[i] > t:
               return
           elif i > 0 and nums[i] == nums[i-1]:
               continue
           elif nums[i] == t:
               ans.append(sel + [nums[i]])
               return
           #elif i == 1 and sel and sel[-1] == nums[0]:
           #    return
           else:
               self.search(nums[i + 1:], sel + [nums[i]], t - nums[i], ans)

sln = Solution()
print sln.combinationSum2([2,2,2],4)
               
    