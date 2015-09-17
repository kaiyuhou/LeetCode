# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:04:58 2015

@author: Mike
"""

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = ['0' for i in range(32)]
        b = bin(n)[2:]        
        m[:len(b)] = b[::-1]
        return int(''.join(m) ,2)
        
sln = Solution()
print sln.reverseBits(43261596)