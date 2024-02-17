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


MOD = 1000000007

# class Solution:
#     def countDaysTogether(self, A1: str, A2: str, B1: str, B2: str) -> int:
#         MD = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#         def TtoD(T):
#             M = int(T[:2])
#             D = int(T[3:])
#             ans = sum(MD[:M])
#             return ans + D

#         A1, A2, B1, B2 = map(TtoD, [A1, A2, B1, B2])
#         A2 += 1
#         B2 += 1
#         ans = min(B2, A2) - max(A1, B1)
#         return max(0, ans)
        
# class Solution:
#     def matchPlayersAndTrainers(self, P: List[int], T: List[int]) -> int:
#         P.sort()
#         T.sort()
#         idx = 0
#         n = len(T)
#         ans = 0
#         for p in P:
#             while idx < n and T[idx] < p:
#                 idx += 1
#             if idx >= n:
#                 break
#             ans += 1
#             idx += 1
#             if idx >= n:
#                 break
#         return ans


# class Solution:
#     def smallestSubarrays(self, A: List[int]) -> List[int]:
#         n = len(A)
#         dp = [[-1] * n for _ in range(30)]
#         for sh in range(30):
#             cur = -1
#             for i in range(n - 1, -1, -1):
#                 if ((1 << sh) & A[i]):
#                     cur = i
#                 dp[sh][i] = cur
#         ans = []
#         for i in range(n):
#             maxn = i
#             for sh in range(30):
#                 maxn = max(maxn, dp[sh][i])
#             ans.append(maxn - i + 1)
#         return ans

class Solution:
    def minimumMoney(self, T: List[List[int]]) -> int:
        pos = []
        max_pos = 0
        max_pos_i = -1
        max_neg = 0
        ans = 0
        for a, b in T:
            if b == 0:
                ans += a
            elif a <= b:
                max_neg = max(max_neg, a)
            else:
                pos.append((a, b))
                if b > max_pos:
                    max_pos = b
                    max_pos_i = len(pos) - 1
        # if max_neg >= max_pos:
        #     ans += max_neg
        #     for a, b in pos:
        #         ans += a - b
        # else:
        for i in range(len(pos)):
            if i == max_pos_i:
                continue
            ans += pos[i][0] - pos[i][1]
        if max_pos_i != -1:
            ans += pos[max_pos_i][0]
        ans += max(0, max_neg - max_pos)
        return ans
        
T = [[6,5],[0,5],[8,5],[3,6],[9,0],[10,1],[4,10]]
# T = [[2,1],[5,0],[4,2]]
T = [[3,0],[0,3]]
s = Solution()
print(s.minimumMoney(T))


























































        

















