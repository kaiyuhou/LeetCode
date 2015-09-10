# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 14:58:55 2015

@author: Mike
"""

class Solution(object):
    def reverse(self, x):
        flag = 1
        if x < 0:
            flag = -1
            x *= -1
        
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x /= 10
        
        if result > 0x7fffffff:
            return 0
            
        return flag * result
        
sln = Solution()
print sln.reverse(-123)