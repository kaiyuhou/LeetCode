# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:44:42 2015

@author: Mike
"""

class Solution(object):
    def buildNext(self, s):
        nxt = [-1]
        i = 0
        t = -1
        while i < len(s) - 1 :
            if t < 0 or s[i] == s[t]:
                i += 1
                t += 1
                nxt.append(nxt[t] if s[i] == s[t] else t)
            else:
                t = nxt[t]
        return nxt
    
    def strStr(self, haystack, needle):
        #return haystack.find(needle)
        #KMP
        nxt = self.buildNext(needle)
        i = 0 #haystack
        j = 0 #needle       
        while i < len(haystack) and j < len(needle) :
            if j < 0 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = nxt[j]
        return i - j if j == len(needle) else -1
        
sln = Solution()
print sln.buildNext('str')
print sln.strStr('rstrststr','str')