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
#     def minMaxGame(self, A: List[int]) -> int:
#         while len(A) > 1:
#             B = []
#             n = len(A)
#             for i in range( n // 2):
#                 if i % 2 == 0:
#                     B.append(min(A[i * 2], A[i * 2 + 1]))
#                 else:
#                     B.append(max(A[i * 2], A[i * 2 + 1]))
#             A = B
#         return A[0]

# class Solution:
#     def partitionArray(self, A: List[int], k: int) -> int:
#         A.sort()
#         ans = 0
#         last = None
#         for a in A:
#             if last is None:
#                 last = a
#                 ans += 1
#             else:
#                 if a - last > k:
#                     last = a
#                     ans += 1
#         return ans



# class Solution:
#     def arrayChange(self, A: List[int], ops: List[List[int]]) -> List[int]:
#         dp = {}
#         for i, a in enumerate(A):
#             dp[a] = i
#
#         for a, b in ops:
#             idx = dp[a]
#             A[idx] = b
#             dp[b] = idx
#
#         return A


class TextEditor:

    def __init__(self):
        self.T = ''
        self.idx = 0

    def addText(self, text: str) -> None:
        n = len(text)
        self.T = self.T[:self.idx] + text + self.T[self.idx:]
        self.idx += n

    def deleteText(self, k: int) -> int:
        k = min(self.idx, k)
        self.T = self.T[:self.idx - k] + self.T[self.idx:]
        self.idx -= k
        return k

    def cursorLeft(self, k: int) -> str:
        self.idx -= k
        self.idx = max(self.idx, 0)
        left = max(0, self.idx - 10)
        return self.T[left:self.idx]

    def cursorRight(self, k: int) -> str:
        n = len(self.T)
        self.idx += k
        self.idx = min(n, self.idx)
        left = max(0, self.idx - 10)
        return self.T[left:self.idx]


te = TextEditor()
te.addText("leetcode")










