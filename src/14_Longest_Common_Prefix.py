# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:22:29 2015

@author: Mike
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ''
        if strs == [] :
            return result
        
        
        shortest = len(strs[0])
        for s in strs:
            shortest = len(s) if len(s) < shortest else shortest
                
        i = 0
        flag = 1
        while flag and i < shortest:
            c = strs[0][i]
            for j in range(1,len(strs)):
                if not c == strs[j][i]:
                    flag = 0
                    break
            if flag:
                result += c
            i += 1
        return result
        
sln = Solution()
testcase = ['abc','abcdf','abcdef']
print sln.longestCommonPrefix(testcase)
        