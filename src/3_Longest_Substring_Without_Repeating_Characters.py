# -*- coding: utf-8 -*-
"""
Created on Fri Oct 09 11:31:47 2015

@author: Mike
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = [-1 for i in range(128)]
        ans = 0
        last = -1
        for (i,ch) in enumerate(s):
            ans = max(i - max(m[ord(ch)],last),ans)
            last = max(last,m[ord(ch)])
            m[ord(ch)] = i
        return ans

sln = Solution()
print sln.lengthOfLongestSubstring("ggububgvfk")