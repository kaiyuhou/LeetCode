# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:34:53 2015

@author: Mike
"""

class Solution(object):
    def process(self, n):
        return sum([int(i) ** 2 for i in str(n)])
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        unhappyset = (1,2,4,16,37,58,89,145,42,20,3,9,81,65,61,5,25,29,85,6,36,45,41,17,50,25,8,64,52)
        while n not in unhappyset:
            n = self.process(n)
        return n == 1
        
sln = Solution()
print sln.isHappy(8)