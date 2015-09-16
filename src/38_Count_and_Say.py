# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:29:57 2015

@author: Mike
"""

class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return '1'
        last = '1#'
        for i in range(2,n+1):
            result = ''
            occur = 1
            for j,c in enumerate(last[1:]):
                if c == last[j]:
                    occur += 1
                else:
                    result += str(occur) + last[j]
                    occur = 1
            last = result + '#'
        return result
        
sln = Solution()
print sln.countAndSay(5)