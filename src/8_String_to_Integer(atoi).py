# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:24:24 2015

@author: Mike
"""

class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        
        print s
        if s == "":
            return 0
        
        if s[0] not in {'-', '+'}  and not s[0].isdigit():
            return 0
        else:
            sign = '+'
            if s[0] in {'-', '+'}:
                sign = s[0]
                s = s[1:]
            
            result = 0
            for c in s:
                if not c.isdigit():
                    break
                result = 10 * result + int(c)
            
            return min(result, 0x7fffffff) if sign == '+' else max(0-result, -2147483648)
            
sln = Solution()
print sln.myAtoi('    010')