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
#     def arithmeticTriplets(self, A: List[int], diff: int) -> int:
#         ans = 0
#         n = len(A)
#         for i in range(n - 2):
#             for j in range(i + 1, n - 1):
#                 if A[j] - A[i] == diff:
#                     for k in range(j + 1, n):
#                         if A[k] - A[j] == diff:
#                             ans += 1
#         return ans


# class Solution:
#     def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
#         R = set(restricted)
#         neighbor = [[] for _ in range(n)]
#         for a, b in edges:
#             neighbor[a].append(b)
#             neighbor[b].append(a)
#         ans = 0
#         V = [False] * n
#         nxt = [0]
#         while nxt:
#             cur = nxt.pop(0)
#             if V[cur]:
#                 continue
#             V[cur] = True
#             ans += 1
#             for b in neighbor[cur]:
#                 if V[b] or b in R:
#                     continue
#                 nxt.append(b)
#         return ans

# class Solution:
#     def validPartition(self, B: List[int]) -> bool:
#
#         dp = {}
#         dp[0] = False
#         dp[-1] = True
#         if B[0] == B[1]:
#             dp[1] = True
#         else:
#             dp[1] = False
#         for i in range(2, len(B)):
#             if B[i] == B[i - 1] and dp[i - 2]:
#                 dp[i] = True
#                 continue
#             if B[i] == B[i - 1] == B[i - 2] and dp[i - 3]:
#                 dp[i] = True
#                 continue
#             if B[i] == B[i - 1] + 1 and B[i] == B[i - 2] + 2 and dp[i - 3]:
#                 dp[i] = True
#                 continue
#             dp[i] = False
#         # print(dp)
#         return dp[len(B) - 1]
#
#
# s = Solution()
# nums = [4,4,4,5,6]
# nums = [1,1,1,2]
# nums = [3,3,3,3,4,5,6,6,7,8]
# print(s.validPartition(nums))


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        A = [ord(c) - ord('a') for c in s]
        last = {i: -1 for i in range(26)}
        dp = {}
        dp[-1] = 0
        for i, a in enumerate(A):
            dp[i] = 1
            for j in range(k + 1):
                if a - j >= 0:
                    last_idx = last[a - j]
                    dp[i] = max(dp[i], dp[last_idx] + 1)
                if a + j < 26:
                    last_idx = last[a + j]
                    dp[i] = max(dp[i], dp[last_idx] + 1)
            last[a] = i
        # print(dp)
        return max(dp.values())

ss = Solution()
s = "acfgbd"
k = 2
print(ss.longestIdealString(s, k))


















































