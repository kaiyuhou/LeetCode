# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 17:28:58 2015

@author: Mike
"""

class Solution(object):
    def romanToInt(self, s):
        dic = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        result = dic[s[-1]]        
        for i in range(0,len(s) - 1):
            result = result + dic[s[i]] if dic[s[i]] >= dic[s[i+1]] else result - dic[s[i]]             
        return result
        
sln = Solution()
print sln.romanToInt('IV')
                