# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:29:14 2015

@author: Mike
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        record = {}
        word = str.split(' ')
        if len(word) != len(pattern):
            return False
        for i,c in enumerate(pattern):
            if c in record:
                if record[c] != word[i]:
                    return False
            elif word[i] in record.values():
                return False
            else:
                record[c] = word[i]
        return True
    
sln = Solution()
print sln.wordPattern('abba','dog dog dog dog')