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
#     def removeAnagrams(self, A: List[str]) -> List[str]:
#         n = len(A)
#         cur = 0
#         ans = [A[0]]
#         for i in range(1, n):
#             if sorted(A[cur]) == sorted(A[i]):
#                 continue
#             else:
#                 cur = i
#                 ans.append(A[i])
#         return ans

# class Solution:
#     def maxConsecutive(self, bottom: int, top: int, A: List[int]) -> int:
#         A.sort()
#         a1 = A[0] - bottom
#         a2 = top - A[-1]
#         ans = max(a1, a2)
#         for i in range(len(A) - 1):
#             cur = A[i + 1] - A[i] - 1
#             ans = max(cur, ans)
#         return ans


# class Solution:
#     def largestCombination(self, candidates: List[int]) -> int:
#         dp = [0] * 30
#         for a in candidates:
#             for i in range(30):
#                 if ((1 << i) & a) > 0:
#                     dp[i] += 1
#         return max(dp)
#
# s = Solution()
# candidates = [16,17,71,62,12,24,14]
# print(s.largestCombination(candidates))
#

import bisect

class CountIntervals:

    def __init__(self):
        self.end = {0: 0}
        self.start = [0]
        self.ans = 0

    def add(self, left: int, right: int) -> None:
        start_i = bisect.bisect(self.start, left) - 1
        start_num = self.start[start_i]
        end_i = bisect.bisect(self.start, right) - 1
        end_num = self.start[end_i]

        if start_i == end_i:
            if left > self.end[start_num]:
                self.ans += right - left + 1
                bisect.insort(self.start, left)
                self.end[left] = right
            elif right <= self.end[start_num]:
                return
            else:
                self.ans += right - self.end[start_num]
                self.end[start_num] = right
            return

        right = max(right, self.end[end_num])
        self.ans += right - left + 1
        if left <= self.end[start_num]:
            self.ans -= self.end[start_num] - left + 1
            for i in range(start_i + 1, end_i + 1):
                cur_num = self.start[i]
                self.ans -= self.end[cur_num] - cur_num + 1
            self.start = self.start[:start_i + 1] + self.start[end_i + 1:]
            self.end[start_num] = right
        else:
            for i in range(start_i + 1, end_i + 1):
                cur_num = self.start[i]
                self.ans -= self.end[cur_num] - cur_num + 1
            self.start = self.start[:start_i + 1] + self.start[end_i + 1:]
            bisect.insort(self.start, left)
            self.end[left] = right

    def count(self) -> int:
        return self.ans


C = CountIntervals()
C.add(2, 3)
print(C.count())
C.add(7, 10)
print(C.count())
C.add(5, 8)
print(C.count())
print(C.start, C.end)
C.add(1, 11)
print(C.count())
print(C.start, C.end)























