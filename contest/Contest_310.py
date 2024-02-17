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
#     def mostFrequentEven(self, nums: List[int]) -> int:
#         A = [a for a in nums if a % 2 == 0]
#         if not A:
#             return -1
#         C = collections.Counter(A)
#         maxn = 0
#         ans = -1
#         for k, v in C.items():
#             if v > maxn:
#                 ans, maxn = k, v
#             elif v == maxn and k < ans:
#                 ans = k

#         return ans

# class Solution:
#     def partitionString(self, s: str) -> int:
#         ans = 0
#         st = set()
#         for c in s:
#             if c in st:
#                 ans += 1
#                 st = set()
#             st.add(c)
#         return ans + 1

# class Solution:
#     def minGroups(self, intervals: List[List[int]]) -> int:
#         A = [0] * 1000005
#         B = set()

#         for a, b in intervals:
#             A[a] += 1
#             A[b + 1] -= 1
#             B.add(a)
#             B.add(b + 1)
        
#         B = list(B)
#         B.sort()

#         ans = 0
#         cur = 0
#         for b in B:
#             if A[b]:
#                 cur += A[b]
#                 ans = max(ans, cur)
#         return ans


# A = [[441459,446342],[801308,840640],[871890,963447],[228525,336985],[807945,946787],[479815,507766],[693292,944029],[751962,821744]]


class SEG:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * self.n
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])

    def query(self, l, r):
        l += self.n
        r += self.n
        ans = 0
        while l < r:
            # If l, the left interval border, is odd 
            # (which is equivalent to l&1) 
            # then l is the right child of its parent. 
            # Then our interval includes node l but doesn't include it's parent.
            # So we check tree[l] and move to the right of l's parent 
            # by setting l = (l + 1) / 2. 
            # If l is even, it is the left child, 
            # and the interval includes its parent as well
            # (unless the right border interferes), 
            # so we just move to it by setting l = l / 2.
            if l & 1:
                ans = max(ans, self.tree[l])
                l += 1
            if r & 1: 
                r -= 1
                ans = max(ans, self.tree[r])
            l >>= 1
            r >>= 1
        return ans

class Solution:
    def lengthOfLIS(self, A: List[int], k: int) -> int:
        n, ans = max(A), 1
        seg = SEG(n)
        for a in A:
            a -= 1
            premax = seg.query(max(0, a - k), a)
            ans = max(ans, premax + 1)
            seg.update(a, premax + 1)
        return ans


A = [7,4,5,1,8,12,4,7]
k = 5
s = Solution()
print(s.lengthOfLIS(A, k))













