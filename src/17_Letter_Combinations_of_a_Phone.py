# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 09:06:34 2015

@author: Mike
"""

class Solution(object):
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return [] 
        dic = {'2':'abc','3':'def','4':'ghi',
               '5':'jkl','6':'mno','7':'pqrs',
               '8':'tuv','9':'wxyz'}
        if len(digits) == 1:
            return list(dic[digits])
        
        temp = self.letterCombinations(digits[0:-1])
        ans = []
        for c in dic[digits[-1]]:
            ans += [s + c for s in temp ]
        return ans
        
sln = Solution()
print sln.letterCombinations('234')
            
                
        