import collections
import heapq
from typing import *
from collections import *
from math import *

from Tree import *

def get_mask(word):
    return sum(1 << (ord(c) - ord("a")) for c in word)


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.weight = [1 for _ in range(n)]

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            if self.weight[pu] < self.weight[pv]:
                self.parent[pu] = pv
                self.weight[pv] = self.weight[pu] + self.weight[pv]
            else:
                self.parent[pv] = pu
                self.weight[pu] = self.weight[pu] + self.weight[pv]

# You are given an n x n square matrix of integers grid. Return the matrix such that:

# The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
# The diagonals in the top-right triangle are sorted in non-decreasing order.

# class Solution:
#     def sortMatrix(self, A: List[List[int]]) -> List[List[int]]:
#         n = len(A)

#         for i in range(0, n):
#             B = []
#             for j in range(0, n - i):
#                 x = i + j
#                 y = j
#                 B.append(A[x][y])
#             B.sort(reverse=True)
#             for j in range(0, n - i):
#                 x = i + j
#                 y = j
#                 A[x][y] = B[j]

#         for j in range(1, n):
#             B = []
#             for i in range(0, n - j):
#                 x = i
#                 y = i + j
#                 B.append(A[x][y])
#             B.sort()
#             for i in range(0, n - j):
#                 x = i
#                 y = i + j
#                 A[x][y] = B[i]

#         return A

# s = Solution()
# grid = [[1,7,3],[9,8,2],[4,5,6]]
# print(s.sortMatrix(grid))

# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         A3 = [0] * 3
#         A9 = [0] * 9
#         ans = []

#         for i, c in enumerate(s):
#             num = ord(c) - ord('0')
#             if num == 0:
#                 ans.append(0)
#             elif num == 1:
#                 ans.append(i + 1)
#             elif num == 2:
#                 ans.append(i + 1)
#             elif num == 3:
#                 ans.append(A3[0] + 1)
#             elif num == 4:
#                 cnt = 1
#                 if i > 0:
#                     if s[i - 1] in ('0', '2', '4', '6', '8'):
#                         cnt += i
#                 ans.append(cnt)
#             elif num == 5:
#                 ans.append(i + 1)
#             elif num == 6:
#                 ans.append(A3[0] + 1)
#             elif num == 7:
#                 cnt = 1
#                 for j in range(i-1, -1, -1):
#                     if s[j] == 7:
#                         if int(s[j:i+1]) % 7 == 0:
#                             cnt += ans[j]
#                         break
#                     if int(s[j:i + 1]) % 7 == 0:
#                         cnt += 1
#                 ans.append(cnt)
#             elif num == 8:
#                 cnt = 1
#                 if i > 0:
#                     if int(s[i - 1:i + 1]) % 8 == 0:
#                         cnt += 1
#                 if i > 1:
#                     if int(s[i - 2:i + 1]) % 8 == 0:
#                         cnt += i - 1
#                 ans.append(cnt)
#             elif num == 9:
#                 ans.append(A9[0] + 1)

#             # print(num, ans[-1])
#             # print(A3)
#             # print(A9)

#             B3 = [0] * 3
#             B9 = [0] * 9
#             for i in range(3):
#                 B3[i] = A3[(i - num) % 3]
#             B3[num % 3] += 1
#             for i in range(9):
#                  B9[i] = A9[(i - num) % 9]
#             B9[num % 9] += 1
#             A3 = B3
#             A9 = B9

            
#         return sum(ans)

# S = Solution()
# s = "12936"
# s = "5701283"
# s = "1010101010"
# s = "217559780313"
# print(S.countSubstrings(s))

# class Solution:
#     def assignElements(self, G: List[int], E: List[int]) -> List[int]:
#         dp = {}
#         maxG = max(G)
#         for i, e in enumerate(E):
#             if e in dp:
#                 continue
#             for j in range(e, maxG + 1, e):
#                 if j not in dp:
#                     dp[j] = i
#         ans = [dp[g] if g in dp else -1 for g in G]
#         return ans

# s = Solution()
# groups = [8,4,3,2,4]
# elements = [4,2]
# print(s.assignElements(groups, elements))

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * 10 for _ in range(10)]
        ans = 0
        for c in map(int, s):
            for i in range(1, 10):
                cnts = [0] * 10
                cnts[c % i] += 1
                for j in range(i):
                    cnts[(j * 10 + c) % i] += dp[i][j]
                dp[i] = cnts
            ans += dp[c][0]
        return ans






