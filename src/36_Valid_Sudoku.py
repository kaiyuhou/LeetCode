# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:55:53 2015

@author: Mike
"""

class Solution(object):
    def isValidSudoku(self, b):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        count = 10
        board = [[0 for j in range(9)] for i in range(9)]
        for i in range(0,9):
            for j in range(0,9):
                if b[i][j] == '.':
                    board[i][j] = count
                    count += 1
                else:
                    board[i][j] = int(b[i][j])
         
        for i in range(0,9):
            r = {0}
            c = {0}            
            for j in range(0,9):
                r.add(board[i][j])
                c.add(board[j][i])
            if len(r) < 10 or len(c) < 10 :
                return False
        
        for i in range(0,3):
            for z in range(0,3):
                block = {0}
                for j in range(i * 3, i * 3 + 3):
                    for k in range(z * 3, z * 3 + 3):
                        block.add(board[j][k])
                if len(block) < 10 :
                    return False
        
        return True
        
#class Solution(object):
#    def isValidSudoku(self, board):
#        """
#        :type board: List[List[str]]
#        :rtype: bool
#        """
#        big = set()
#        for i in xrange(0,9):
#            for j in xrange(0,9):
#                if board[i][j]!='.':
#                    cur = board[i][j]
#                    if (i,cur) in big or (cur,j) in big or (i/3,j/3,cur) in big:
#                        return False
#                    big.add((i,cur))
#                    big.add((cur,j))
#                    big.add((i/3,j/3,cur))
#        return True
        
sln = Solution()
print sln.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])