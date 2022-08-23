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
#     def largestLocal(self, A: List[List[int]]) -> List[List[int]]:
#         n = len(A)
#         n -= 2
#         ans = [[0] * n for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 ans[i][j] = max(A[i][j], A[i][j + 1], A[i][j + 2],
#                                 A[i+1][j], A[i+1][j + 1], A[i+1][j + 2],
#                                 A[i+2][j], A[i+2][j + 1], A[i+2][j + 2])
#         return ans

# class Solution:
#     def edgeScore(self, edges: List[int]) -> int:
#         n = len(edges)
#         ans = [0] * n
#         for i, nei in enumerate(edges):
#             ans[nei] += i
#         mx = max(ans)
#         return ans.index(mx)

# class Solution:
#     def smallestNumber(self, P: str) -> str:
#         V = [False] * 10
#         n = len(P) + 1
#         ans = [0] * n
#         ans[0] = 1
#         V[1] = True
#         for i in range(1, n):
#             if P[i - 1] == 'I':
#                 for j in range(ans[i - 1] + 1, 10):
#                     if not V[j]:
#                         V[j] = True
#                         ans[i] = j
#                         break
#             else:
#                 ans[i] = ans[i - 1]
#                 j = i - 2
#                 while j >= 0 and P[j] == 'D':
#                     ans[j + 1] = ans[j]
#                     j -= 1
#                 for k in range(1, 10):
#                     if not V[k]:
#                         V[k] = True
#                         ans[j + 1] = k
#                         break
#         return ''.join(map(str, ans))

# s = Solution()
# P = "III"
# P = "DDD"
# P = "IIIDIDDI"
# print(s.smallestNumber(P))


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        S = str(n)
        ans = 0
        n = len(S)
        used = set()

        for i in range(1, n):
            cur_ans = 9
            for j in range(i, n - 1):
                cur_ans *= 9 - (j - i)
            ans += cur_ans

        if int(S[0]) > 1:
            cur_ans = int(S[0]) - 1
            for i in range(0, n - 1):
                cur_ans *= 9 - i
            ans += cur_ans

        used.add(int(S[0]))

        for i in range(1, n):
            if len(S[:i]) != len(set(S[:i])):
                break

            cur = int(S[i])
            base = 0

            for j in range(0, cur):
                if j not in used:
                    base += 1

            for j in range(i + 1, n):
                base *= 10 - j
            ans += base
            used.add(cur)

        if len(S) == len(set(S)):
            ans += 1
        return ans








def check(n):
    ans = 0
    for i in range(1, n + 1):
        if len(str(i)) == len(set(str(i))):
            ans += 1
    return ans



s = Solution()
# print(s.countSpecialNumbers(11))

for i in range(1, 2000):
    if s.countSpecialNumbers(i) != check(i):
        print(i, s.countSpecialNumbers(i), check(i))




















































