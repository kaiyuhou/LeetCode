# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:13:31 2015

@author: Mike
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)):
            return False
        dict = {}
        for i in range(0,len(t)):
            if s[i] in dict:
                if dict[s[i]] != t[i]:
                    return False
            else:
                dict[s[i]] = t[i]
        return True
        
sln = Solution()
print sln.isIsomorphic("ab","aa")