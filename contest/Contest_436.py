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
#     def hasSpecialSubstring(self, s: str, k: int) -> bool:
#         pre = ''
#         cnt = 0
#         dp = set()
#         for c in s:
#             if pre == c:
#                 cnt += 1
#             else:
#                 dp.add(cnt)
#                 pre = c
#                 cnt = 1
#         dp.add(cnt)
#         return k in dp 

# class Solution:
#     def maxWeight(self, P: List[int]) -> int:
#         ans = 0
#         n = len(P) // 4
#         odd = (n + 1) // 2
#         even = n - odd

#         P.sort(reverse=True)
#         P = P[:n*2]
#         ans += sum(P[:odd])
#         P = P[odd:-odd]
#         for i in range(even):
#             ans += P[i * 2 + 1]
#         return ans


class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        start = {}
        end = {}
        count = Counter()

        for i, c in enumerate(s):
            start.setdefault(c, i)
            end[c] = i
            count[c] += 1

        seps = []
        for c1, i in start.items():
            for c2, j in end.items():
                if i <= j:
                    cnt = 0
                    for c in count:
                        if i <= start[c] <= end[c] <= j:
                            cnt += count[c]
                    if cnt == j - i + 1 and cnt < len(s):
                        seps.append([i, j])

        seps.sort(key = lambda s: s[1] - s[0])
        ans = []
        for i, j in seps:
            if all(y < i or j < x for x, y in ans):
                ans.append([i, j])
        return len(ans) >= k
        





















