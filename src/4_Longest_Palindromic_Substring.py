# -*- coding: utf-8 -*-
"""
Created on Fri Oct 09 16:55:51 2015

@author: Mike
"""

class Solution(object):
    def longestPalindrome(self, s):
        s = '#'.join('$' + s) + '#@'
        p = [0 for i in range(len(s))]
        mx, idx, ans = 0, 0, 0
        for i in range(1,len(s) - 1):
            p[i] = min(p[2 * idx - i], mx - i) if mx > i else 1
            while s[i + p[i]] == s[i - p[i]]:
                p[i] += 1
            if i + p[i] > mx:
                mx = i + p[i]
                idx = i
            if p[i] > p[ans]:
                ans = i
        return s[ans - (p[ans] - 2):ans + p[ans]:2]

sln = Solution()
print sln.longestPalindrome('abcbadefffed')