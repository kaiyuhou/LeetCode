# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:43:40 2016

@author: Mike
"""

class Solution(object):
    def rotate(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(m)
        for i in range((l+1)/2):
            for j in range(l/2):
                #m[i][j], m[j][l-i-1], m[l-i-1][l-j-1],m[l-j-1][i] 
                #= m[l-j-1][i], m[i],[j],m[j][l-i-1], m[l-i-1][l-j-1]
                t = m[i][j]
                m[i][j] = m[l-j-1][i]  
                m[l-j-1][i] = m[l-i-1][l-j-1]
                m[l-i-1][l-j-1] = m[j][l-i-1]
                m[j][l-i-1] = t
                
        #print m
sln = Solution()
sln.rotate([[1,2,3],[4,5,6],[7,8,9]])