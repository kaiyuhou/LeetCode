# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:46:45 2015

@author: Mike
"""

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        x: A C E G
        y: B D F H
        :rtype: int
        """
        total = (C - A)*(D - B) + (G - E)*(H - F)
        if (A > G) or (B >H) or (C < E) or (D < F):
            return total
        x1 = max(A,E)
        x2 = min(C,G)
        y1 = max(B,F)
        y2 = min(D,H)
        return total - (x2-x1)*(y2-y1)
        
sln = Solution()
print sln.computeArea(-3,0,3,4,0,-1,9,2)