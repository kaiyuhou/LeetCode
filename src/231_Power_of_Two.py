# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 09:52:07 2015

@author: Mike
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return True if n>0 and (n&(n-1)) == 0 else False
sln = Solution()
print sln.isPowerOfTwo(1)