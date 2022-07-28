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


# class Solution:
#     def removeDigit(self, number: str, digit: str) -> str:
#         ans = ''
#         best = 0
#         for i, c in enumerate(number):
#             if c == digit:
#                 cur = number[:i] + number[i + 1:]
#                 if int(cur) > best:
#                     best = int(cur)
#                     ans = cur
#         return ans

# class Solution:
#     def minimumCardPickup(self, cards: List[int]) -> int:
#         ans = -1
#         dp = {}
#         for i, c in enumerate(cards):
#             if c in dp:
#                 cur = i - dp[c] + 1
#                 if ans == -1:
#                     ans = cur
#                 elif cur < ans:
#                     ans = cur
#             dp[c] = i
#         return ans

# class Solution:
#     def countDistinct(self, nums: List[int], k: int, p: int) -> int:
#         cnt = 0
#         cur = []
#         ans = set()
#         for i, a in enumerate(nums):
#             cur.append(a)
#             if a % p == 0:
#                 cnt += 1
#             while cnt > k:
#                 left = cur.pop(0)
#                 if left % p == 0:
#                     cnt -= 1
#             for j in range(len(cur) - 1, -1, -1):
#                 ans.add(tuple(cur[j:]))
#         return len(ans)
#
#
# s = Solution()
# nums = [2,3,3,2,2]
# k = 2
# p = 2
# print(s.countDistinct(nums, k, p))


class Solution:
    def appealSum(self, s: str) -> int:
        pos = {}
        last = 0
        ans = 0
        for i, c in enumerate(s):
            if c in pos:
                ex = i - pos[c]
            else:
                ex = i + 1
            pos[c] = i

            last = ex + last
            ans += last
        return ans



























