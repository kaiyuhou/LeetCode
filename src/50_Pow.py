# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:12:25 2016

@author: Mike
"""

class Solution(object):
    def iterPow(self, x, n):
        if n == 1:
            return x
        if n == 0:
            return 1
        ans = x if n % 2 == 1 else 1;
        temp = self.iterPow(x, n/2)
        return ans * temp * temp
    
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans = self.iterPow(x, abs(n))
        return ans if n >=0 else 1/ans
        

sln = Solution()
print sln.myPow(2,7)
            