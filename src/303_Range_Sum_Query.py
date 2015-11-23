# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:29:21 2015

@author: Mike
"""

class NumArray(object):

    def __init__(self, nums):
        self.record = [0]
        lastSum = 0        
        for i in nums:
            lastSum += i
            self.record.append(lastSum)
        
    def sumRange(self, i, j):
        return self.record[j + 1] - self.record[i] 
        
sln = NumArray([-1])
print sln.sumRange(0,0)
#print sln.sumRange(2,5)