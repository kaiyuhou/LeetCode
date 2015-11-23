# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:15:58 2015

@author: Mike
"""

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        num = [0 for i in range(10)]
        isDel = [0 for i in range(len(guess))]
        bull = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
                isDel[i] = 1
            else:
                num[int(secret[i])] += 1
        
        cows = 0        
        for i in range(len(guess)):
            if isDel[i]:
                continue
            if num[int(guess[i])] > 0:
                cows += 1
                num[int(guess[i])] -= 1
                
        return str(bull) + 'A' + str(cows) + 'B'
        
sln = Solution()
print sln.getHint('1123','0111')