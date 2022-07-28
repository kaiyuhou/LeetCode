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
#     def greatestLetter(self, s: str) -> str:
#         C = collections.Counter(s)
#         baseLow = ord('z')
#         baseUp = ord('Z')
#         for i in range(26):
#             low = chr(baseLow - i)
#             up = chr(baseUp - i)
#             if low in C and up in C:
#                 return up
#         return ''


# class Solution:
#     def minimumNumbers(self, num: int, k: int) -> int:
#         if num == 0:
#             return 0
#
#         last = num % 10
#         for i in range(1, 11):
#             if (k * i) % 10 == last:
#                 if k * i <= num:
#                     return i
#         return -1
#
#
# s = Solution()
# num = 10
# k = 1
# print(s.minimumNumbers(num, k))

# class Solution:
#     def longestSubsequence(self, s: str, k: int) -> int:
#         C = collections.Counter(s)
#         ans = C['0']
#         s = s[::-1]
#         cur = 0
#         for i, c in enumerate(s):
#             if c == '1':
#                 cur += 2 ** i
#                 if cur <= k:
#                     ans += 1
#                 else:
#                     break
#         return ans

from functools import lru_cache
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        P = {}
        small_h = m
        small_n = n
        small_a = m * n
        h_list = set()
        n_list = set()
        for h, w, p in prices:
            P[h, w] = p
            h_list.add(h)
            n_list.add(w)
            small_h = min(h, small_h)
            small_n = min(w, small_n)
            small_a = min(small_a, h * w)

        h_list = list(h_list)
        n_list = list(n_list)
        h_list.sort()
        n_list.sort()
        h_list = tuple(h_list)
        n_list = tuple(n_list)
        # print(small_h, small_n, small_a)

        @lru_cache(None)
        def cut(x, y):
            if x * y < small_a:
                return 0

            if x < small_h or y < small_n:
                return 0

            ans = 0
            if (x, y) in P:
                ans = P[x, y]

            if y >= small_n and x > small_h:
                for h in h_list:
                    if h < x:
                        ans = max(ans, cut(h, y) + cut(x - h, y))
                    else:
                        break

            if x >= small_h and y > small_n:
                for w in n_list:
                    if w < y:
                        ans = max(ans, cut(x, w) + cut(x, y - w))
                    else:
                        break

            return ans

        return cut(m, n)


s = Solution()
m = 200
n = 200
prices = [[1,1,2],[2,2,7],[2,1,3]]
# m = 8
# n = 2
# prices = [[5,2,9],[6,1,30]]


print(s.sellingWood(m, n, prices))



































