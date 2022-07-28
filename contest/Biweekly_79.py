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
#     def digitCount(self, num: str) -> bool:
#         C = collections.Counter(num)
#         for i, a in enumerate(num):
#             if C[str(i)] == int(a):
#                 continue
#             else:
#                 return False
#         return True

# class Solution:
#     def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
#         C = collections.Counter()
#         n = len(messages)
#         for i in range(n):
#             C[senders[i]] += len(messages[i].split())
#         ans = None
#         for i, k in C.items():
#             if ans is None:
#                 ans = i
#             elif k > C[ans]:
#                 ans = i
#             elif k == C[ans] and i > ans:
#                 ans = i
#         return ans


# class Solution:
#     def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
#         A = [0] * n
#         for a, b in roads:
#             A[a] += 1
#             A[b] += 1
#         A.sort()
#         ans = 0
#         for i, a in enumerate(A):
#             ans += (i + 1) * a
#         return ans

import bisect
class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.A = [m] * n
        block = (n + 199) // 200
        self.B = [0] * block
        for i in range(block):
            if i < block - 1:
                self.B[i] = 200 * m
            else:
                self.B[i] = (n % 200) * m
        self.start_idx = 0
        self.start_block = 0
        self.MAX = [(m, 0), (m + 1, n)]

    def get(self, idx):
        if idx < self.start_idx:
            return 0
        block = idx // 200
        if block < self.start_block:
            return 0
        if self.B[block] == 0:
            return 0
        return self.A[idx]

    def sum(self, idx):
        ans = 0
        block = idx // 200
        for i in range(self.start_block, block):
            ans += self.B[i]
        for i in range(block * 200, idx + 1):
            ans += self.get(i)
        return ans

    def gather(self, k: int, maxRow: int) -> List[int]:
        if k > self.m:
            return []
        i = bisect.bisect_left(self.MAX, (k, 0))
        idx = self.MAX[i][1]
        if idx > maxRow:
            return []
        ansn = idx
        ansm = self.m - self.A[idx]
        self.A[idx] -= k
        block = idx // 200
        self.B[block] -= k
        left = self.MAX[:idx]
        right = self.MAX[idx + 1:]
        new_MAX = []
        last = None
        if left:
            last = left[-1][0]
        end_idx = right[0][1]
        for i in range(idx, end_idx):
            if last is None:
                last = self.get(i)
                new_MAX.append((last, i))
            elif self.get(i) > last:
                last = self.get(i)
                new_MAX.append((last, i))
            if last == self.m:
                break
        self.MAX = left + new_MAX + right
        return [ansn, ansm]

    def scatter(self, k: int, maxRow: int) -> bool:
        if self.sum(maxRow) < k:
            return False
        block = self.start_block
        while self.B[block] < k:
            k -= self.B[block]
            self.B[block] = 0
            block += 1
        self.start_block = block
        idx = block * 200
        while k > 0:
            if self.get(idx) >= k:
                self.A[idx] -= k
                k = 0
            else:
                k -= self.get(idx)
                self.A[idx] = 0
                idx += 1
        self.start_idx = idx

        for i, (_, x) in enumerate(self.MAX):
            if x >= idx:
                break
        self.MAX = self.MAX[i:]
        end_idx = self.MAX[0][1]
        new_MAX = []
        last = None
        for i in range(self.start_idx, end_idx):
            if last is None:
                last = self.get(i)
                new_MAX.append((last, i))
            elif self.get(i) > last:
                last = self.get(i)
                new_MAX.append((last, i))
            if last == self.m:
                break
        self.MAX = new_MAX + self.MAX
        return True

bms = BookMyShow(2, 5)
print(bms.gather(4, 0))
print(bms.gather(2, 0))
print(bms.scatter(5, 1))
print(bms.scatter(5, 1))














