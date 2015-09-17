# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:20:56 2015

@author: Mike
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            result += n % 2
            n = n>>1
        return result
        #return "{0:b}".format(n).count('1')
        
sln = Solution()
print sln.hammingWeight(11)