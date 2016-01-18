# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 09:41:38 2015

@author: Mike
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.deep(['('],n-1,1)
        
    def deep(self, stepans, n, stack):
        if n == 0:
            return [s + ')' * stack for s in stepans]
        
        ans = []
        for i in range(stack + 1):
            ans += self.deep([s + ')' * i + '(' for s in stepans ], n - 1, stack + 1 - i )
        return ans
        
sln = Solution()
print sln.generateParenthesis(2)