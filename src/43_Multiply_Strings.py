# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:39:25 2016

@author: Mike
"""

class Solution(object):
    def multiply(self, num1, num2):
        ans = [0 for i in range(len(num1) + len(num2))]
        num1, num2 = num1[::-1], num2[::-1]
        
        n1 = [ord(i) - 48 for i in num1 ]
        n2 = [ord(i) - 48 for i in num2 ]
        
        for i in range(len(n1)):
            for j in range(len(n2)):
                ans[i + j]  += n1[i] * n2[j]
                
        for i in range(len(ans) - 1):
            ans[i + 1] += ans[i] / 10
            ans[i] %= 10
        
        res = [chr(i + 48) for i in ans[::-1]]
        while res[0] == '0' and len(res) > 1:
            res.remove('0')
        return "".join(res)
        
sln = Solution()
print sln.multiply("1234","5678")
            