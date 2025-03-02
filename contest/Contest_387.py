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
#     def resultArray(self, C: List[int]) -> List[int]:
#         A = [C[0]]
#         B = [C[1]]
#         for i in range(2, len(C)):
#             if A[-1] > B[-1]:
#                 A.append(C[i])
#             else:
#                 B.append(C[i])
#         return A + B

# class Solution:
#     def countSubmatrices(self, A: List[List[int]], k: int) -> int:
#         n = len(A)
#         m = len(A[0])

#         C = collections.defaultdict(int)
#         L = collections.defaultdict(int)
#         ans = 0
#         for i in range(n):
#             for j in range(m):
#                 L[i, j] = L[i, j - 1] + A[i][j]
#                 C[i, j] = C[i - 1, j] + L[i, j]
#                 if C[i, j] <= k:
#                     ans += 1
#         return ans 

# class Solution:
#     def minimumOperationsToWriteY(self, A: List[List[int]]) -> int:
#         n = len(A)
#         C1 = collections.Counter()
#         C2 = collections.Counter()
#         for i in range(n):
#             for j in range(n):
#                 if i < n // 2:
#                     if i == j:
#                         C1[A[i][j]] += 1
#                     elif i + j == n - 1:
#                         C1[A[i][j]] += 1
#                     else:
#                         C2[A[i][j]] += 1
#                 else:
#                     if j == n // 2:
#                         C1[A[i][j]] += 1
#                     else:
#                         C2[A[i][j]] += 1
#         tot = sum(C1.values()) + sum(C2.values())

#         ans = tot
#         for i in range(3):
#             for j in range(3):
#                 if i == j:
#                     continue
#                 cur = tot - C1[i] - C2[j]
#                 ans = min(ans, cur)
#         return ans

# grid = [[1,2,2],[1,1,0],[0,1,0]]
# print(Solution().minimumOperationsToWriteY(grid))

import bisect
class Solution:
    def resultArray(self, A: List[int]) -> List[int]:
        B = [A[0]]
        C = [A[1]]
        BB = [A[0]]
        CC = [A[1]]

        def gC(A, a):
            i = bisect.bisect_right(A, a)
            return len(A) - i

        for i in range(2, len(A)):
            a = A[i]
            g1 = gC(B, a)
            g2 = gC(C, a)
            if g1 > g2:
                bisect.insort_right(B, a)
                BB.append(a)

            elif g1 < g2:
                bisect.insort_right(C, a)
                CC.append(a)

            elif len(C) < len(B):
                bisect.insort_right(C, a)
                CC.append(a)
            else:
                bisect.insort_right(B, a)
                BB.append(a)
        return BB + CC
            
nums = [2,1,3,3]
print(Solution().resultArray(nums))



        





