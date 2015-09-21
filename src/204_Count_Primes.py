# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 08:40:05 2015

@author: Mike
"""
import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0         
        
        a = [1 for i in range(n)]
        a[0] = 0
        a[1] = 0
        for i in range(2,int(math.sqrt(n))+1):
            if a[i] == 0:
                continue
            j=i
            while i * j < n:
                a[i * j] = 0
                j += 1
        return sum(a)
        
sln = Solution()
print sln.countPrimes(100)