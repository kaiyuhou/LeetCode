# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:29:47 2015

@author: Mike
"""

class Solution(object):
    def addDigits(self, n):
        if n == 0:
            return 0      
        return n - 9 * ((n - 1) / 9)