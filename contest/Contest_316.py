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
#     def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
#         def f(s):
#             return int(s[:2]) * 60 + int(s[3:])
        
#         s1, e1, s2, e2 = f(event1[0]), f(event1[1]), f(event2[0]), f(event2[1])
#         if e2 < s1 or s2 > e1:
#             return False
#         return True


# class Solution:
#     def subarrayGCD(self, nums: List[int], k: int) -> int:
#         ans = 0
#         n = len(nums)
#         for i in range(n):
#             cur = nums[i]
#             for j in range(i, n):
#                 cur = gcd(cur, nums[j])
#                 if cur == k:
#                     ans += 1
#                 elif cur < k:
#                     break
#         return ans

class Solution:
    def minCost(self, A: List[int], C: List[int]) -> int:
        n = len(A)
        def cost(e):
            return sum([abs(A[i] - e) * C[i] for i in range(n)])

        left = min(A)
        right = max(A)
        lcost = cost(left)
        rcost = cost(right)

        while left < right - 1:
            mid = (left + right) // 2
            mcost = cost(mid)
            if lcost < rcost:
                left, right = left, mid
                rcost = mcost
            else:
                left, right = mid, right
                lcost = mcost
        
        return min(lcost, rcost)
        


# class Solution:
#     def makeSimilar(self, A: List[int], T: List[int]) -> int:
#         Aodd, Aeven = [], []
#         for a in A:
#             if a % 2 == 0:
#                 Aeven.append(a)
#             else:
#                 Aodd.append(a)
        
#         Todd, Teven = [], []
#         for t in T:
#             if t % 2 == 0:
#                 Teven.append(t)
#             else:
#                 Todd.append(t)
        
#         Aeven.sort()
#         Aodd.sort()
#         Teven.sort()
#         Todd.sort()

#         plus_cnt, minus_cnt = 0, 0

#         def check(A, T):
#             nonlocal plus_cnt, minus_cnt
#             for i in range(len(A)):
#                 if A[i] < T[i]:
#                     plus_cnt += abs(T[i] - A[i]) // 2
#                 else:
#                     minus_cnt += abs(T[i] - A[i]) // 2
        
#         check(Aeven, Teven)
#         check(Aodd, Todd)

#         return plus_cnt



        











