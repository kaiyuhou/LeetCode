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
#     def maximumLengthSubstring(self, s: str) -> int:
#         ans = 0 
#         n = len(s)
#         for i in range(2, n + 1):
#             for j in range(0, n - i + 1):
#                 if collections.Counter(s[j:j + i]).most_common(1)[0][1] <= 2:
#                     ans = i
#         return ans

# S = Solution()
# s = "bcbbbcba"
# print(S.maximumLengthSubstring(s))

# class Solution:
#     def minOperations(self, k: int) -> int:
#         if k == 1:
#             return 0

#         ans = k - 1
#         for i in range(2, k - 1):
#             n = (k + i - 1) // i
#             cur = n - 1 + i - 1
#             if cur <= ans:
#                 ans = cur
#             else:
#                 break
#         return ans

# s = Solution()
# print(s.minOperations(90000))

# import heapq
# class Solution:
#     def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
#         h = []
#         ans = []
#         heapq.heapify(h)
#         C = collections.Counter()
#         for a, f in zip(nums, freq):
#             C[a] += f
#             heapq.heappush(h, (-C[a], a))
#             while len(h) > 0:
#                 cnt, num = heapq.heappop(h)
#                 if C[num] == -cnt:
#                     ans.append(-cnt)
#                     heapq.heappush(h, (cnt, num))
#                     break
#             else:
#                 ans.append(0)
#         return ans

# s = Solution()
# nums = [2,3,2,1]
# freq = [3,2,-3,1]
# print(s.mostFrequentIDs(nums, freq))

class Node:
     def __init__(self):
        self.ch = {}
        self.idx = -1

class Solution:
    def stringIndices(self, WC: List[str], WQ: List[str]) -> List[int]:
        N = [len(s) for s in WC]
        root = Node()

        minLen = min(N)
        for i, s in enumerate(WC):
            if len(s) == minLen:
                root.idx = i
                break


        for i, s in enumerate(WC):
            cur = root
            for c in s[::-1]:
                if c not in cur.ch:
                    cur.ch[c] = Node()
                    cur.ch[c].idx = i
                else:
                    if N[i] < N[cur.ch[c].idx]:
                        cur.ch[c].idx = i
                cur = cur.ch[c]

        ans = []
        for s in WQ:
            cur = root
            for c in s[::-1]:
                if c in cur.ch:
                    cur = cur.ch[c]
                else:
                    break
            ans.append(cur.idx)
        return ans
                








                

