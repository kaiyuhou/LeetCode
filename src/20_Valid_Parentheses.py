# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:30:01 2015

@author: Mike
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        i = 0
        flag = 1
        while i < len(s):
            if s[i] in {'(','{','['}:
                stack.append(s[i])
            else:
                if stack :
                    top = stack.pop()
                    if ord(s[i]) - ord(top) not in [1,2]:
                        flag = 0
                        break
                else :
                    flag = 0
                    break
            i += 1;    
        return flag == 1 and stack == []

sln = Solution()
print sln.isValid('()')