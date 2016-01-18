# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:41:15 2015

@author: Mike
"""

class Solution(object):
    INT_MAX = 0x7fffffff    
    
    def divide(self, dividend, divisor):
        """
        :type dividend: int 被除数
        :type divisor: int 除数
        :rtype: int
        """
        if dividend == 0:
            return 0
        seg = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ans =0
        while dividend >= divisor:
            x = divisor
            i = 1
            while dividend >= x + x:
                x += x
                i += i
            dividend -= x
            ans += i
        ans = self.INT_MAX if not seg and ans > self.INT_MAX else ans
        return -ans if seg else ans
        
sln = Solution()
print sln.divide(38, -8)
        