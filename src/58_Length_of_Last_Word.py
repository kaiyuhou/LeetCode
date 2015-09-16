# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:11:11 2015

@author: Mike
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        slist = s.strip().split(' ')
        return len(slist[-1])
        
sln = Solution()
print sln.lengthOfLastWord('a ')