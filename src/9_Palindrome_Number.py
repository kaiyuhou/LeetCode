# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 17:20:04 2015

@author: Mike
"""

class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]