# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 09:09:14 2015

@author: Mike
"""

class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)