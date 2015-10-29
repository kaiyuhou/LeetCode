# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 09:01:24 2015

@author: Mike
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        m = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
#        dic = [['M'],
#               ['C','D','M'],
#               ['X','L','C'],
#               ['I','V','X']]        
#        m = [[1],[1,1],[1,1,1],[1,2],[2],[2,1],[2,1,1],[2,1,1,1],[1,3]]
#        ans = ''
#        for (i,v) in enumerate([1000,100,10,1]):
#            if num >= v:
#                ans += "".join([dic[i][j - 1] for j in m[num / v - 1]])
#                num %= v
        ans = ''
        for i in m:
            while num >= i:
                ans += dic[i]
                num -= i
        return ans
        
sln = Solution()
print sln.intToRoman(10)
                