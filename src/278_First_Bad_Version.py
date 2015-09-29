# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:14:16 2015

@author: Mike
"""

class Solution(object):
    def firstBadVersion(self, n):
		l = 1
        r = n
        while r > l:
            m = (l + r) / 2
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1                
            
        return l if isBadVersion(l) else l+1