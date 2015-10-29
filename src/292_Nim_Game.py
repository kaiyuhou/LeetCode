# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:29:04 2015

@author: Mike
"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0:
            return False
        return True
        