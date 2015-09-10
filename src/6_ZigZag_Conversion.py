# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 09:23:53 2015

@author: Mike
"""

class Solution(object):   
    
    def convert(self, s, numRows):
        if s == '' or numRows <= 1 :
            return s
            
        result = ''
        i = 0 # current row
        while (i < len(s) and i < numRows):
            j = i # current pos
            # if the fisrt or last row
            if i == 0 or i == numRows - 1:
                while j < len(s):
                    result += s[j]
                    j += 2 * numRows - 2;
            else:
                k = 1 # is odd column
                while j < len(s):
                    result += s[j]
                    if k:
                        j += 2 * (numRows - 1 - i)
                    else :
                        j += 2 * i
                    k = not k
            i += 1
            
        return result
                        
sln = Solution()
print sln.convert("ABC", 3)