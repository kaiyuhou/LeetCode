# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:54:29 2015

@author: Mike
"""

class Solution(object):
    def isUgly(self, n):
        """
        :type num: int
        :rtype: bool
        """
        if n == 0:
            return False
        
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 ==0:
            n /= 5
        return n == 1