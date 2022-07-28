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
#     def calculateTax(self, brackets: List[List[int]], income: int) -> float:
#         ans = 0
#         last_up = 0
#         for up, percent in brackets:
#             if income > up:
#                 ans += (up - last_up) * percent * 0.01
#             else:
#                 ans += (income - last_up) * percent * 0.01
#                 break
#             last_up = up
#         return ans

# class Solution:
#     def minPathCost(self, A: List[List[int]], C: List[List[int]]) -> int:
#         n = len(A)
#         m = len(A[0])
#
#         for i in range(n - 2, -1, -1):
#             for j in range(m):
#                 ans = None
#                 a = A[i][j]
#                 for k in range(m):
#                     cur = C[a][k] + A[i + 1][k]
#                     if ans is None or cur < ans:
#                         ans = cur
#                 A[i][j] += ans
#         return min(A[0])

# class Solution:
#     def distributeCookies(self, A: List[int], k: int) -> int:
#         ans = sum(A)
#         n = len(A)
#         C = [0] * k
#         A.sort(reverse=True)
#
#         def fun(idx):
#             nonlocal ans
#             if max(C) >= ans:
#                 return
#             if idx == n:
#                 ans = min(ans, max(C))
#                 return
#             for i in range(k):
#                 C[i] += A[idx]
#                 fun(idx + 1)
#                 C[i] -= A[idx]
#
#         C[0] = A[0]
#         fun(1)
#         return ans
#
# s = Solution()
# A = [8,15,10,20,8,9,8,8]
# k = 8
# print(s.distributeCookies(A, k))

class Solution:
    def distinctNames(self, A: List[str]) -> int:
        A_SET = set(A)
        C = collections.Counter()
        A_NOT_B = collections.Counter()
        letter = [chr(97 + i) for i in range(26)]
        for a in A:
            C[a[0]] += 1
            for c in letter:
                if c == a[0]:
                    continue
                if c + a[1:] in A_SET:
                    A_NOT_B[a[0], c] += 1
        # print(C)
        # print(A_NOT_B)

        ans = 0
        for a in A:
            for c in letter:
                if c == a[0]:
                    continue
                if c + a[1:] in A_SET:
                    continue
                ans += C[c] - A_NOT_B[c, a[0]]
                # if C[c]:
                #     print(a, ans)
        return ans

s = Solution()
A = ["coffee","donuts","time","toffee"]
print(s.distinctNames(A))


































































