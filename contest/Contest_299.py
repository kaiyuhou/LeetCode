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
#     def checkXMatrix(self, grid: List[List[int]]) -> bool:
#         n = len(grid)
#         idx = set()
#         for i in range(n):
#             if grid[i][i] == 0:
#                 return False
#             idx.add((i, i))
#
#         for i in range(n):
#             if grid[i][n - i - 1] == 0:
#                 return False
#             idx.add((i, n - i - 1))
#
#         for i in range(n):
#             for j in range(n):
#                 if (i, j) in idx:
#                     continue
#                 if grid[i][j] != 0:
#                     return False
#
#         return True



# MOD = 1000000007
#
# class Solution:
#     def countHousePlacements(self, n: int) -> int:
#         dp = [0] * (n + 1)
#         S = [0] * (n + 1)
#         dp[0] = 1
#         S[0] = 1
#         dp[1] = 1
#         S[1] = 2
#         for i in range(2, n + 1):
#             dp[i] = S[i - 2] % MOD
#             S[i] = S[i - 1] + dp[i]
#
#         ans = sum(dp) % MOD
#         return ans * ans % MOD
#
# s = Solution()
# n = 10000
# print(s.countHousePlacements(n))


# class Solution:
#     def maximumsSplicedArray(self, A: List[int], B: List[int]) -> int:
#         SA = sum(A)
#         SB = sum(B)
#         if SA < SB:
#             SA, SB = SB, SA
#             A, B = B, A
#         n = len(A)
#
#         # print(A)
#         # print(B)
#         # print(SA, SB)
#         # print([A[i] - B[i] for i in range(n)])
#
#         ans = SA
#         extra = 0
#         # cA, cB = SA, SB
#         for i in range(n):
#             extra += B[i] - A[i]
#             # print(i, extra)
#             ans = max(ans, SA + extra)
#             if extra < 0:
#                 extra = 0
#
#         extra = 0
#         for i in range(n):
#             extra += A[i] - B[i]
#             ans = max(ans, SB + extra)
#             if extra < 0:
#                 extra = 0
#         return ans
#
#
# s = Solution()
# A = [28,34,38,14,30,31,23,7,28,3]
# B = [42,35,7,6,24,30,14,21,20,34]
# print(s.maximumsSplicedArray(A, B))


class Solution:
    def minimumScore(self, A: List[int], E: List[List[int]]) -> int:
        n = len(A)
        PA = [-1] * n
        CH = {i: [] for i in range(n)}

        for a, b in E:
            CH[a].append(b)
            CH[b].append(a)

        nxt = [0]
        while nxt:
            cur = nxt.pop(0)
            for ch in CH[cur]:
                CH[ch].remove(cur)
                PA[ch] = cur
                nxt.append(ch)

        PP = {i: set() for i in range(n)}
        def build_PP(root):
            PP[root].add(root)
            for ch in CH[root]:
                PP[root].update(build_PP(ch))
            return PP[root]
        build_PP(0)


        XOR = [0] * n
        def dfs(root):
            ans = A[root]
            for ch in CH[root]:
                ans ^= dfs(ch)
            XOR[root] = ans
            return ans
        dfs(0)

        ans = float('inf')
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                p1, c1 = E[i]
                if PA[p1] == c1:
                    c1, p1 = p1, c1

                p2, c2 = E[j]
                if PA[p2] == c2:
                    c2, p2 = p2, c2

                if c2 in PP[c1]:
                    a = XOR[c2]
                    b = XOR[c1] ^ XOR[c2]
                    c = XOR[0] ^ XOR[c1]
                elif c1 in PP[c2]:
                    a = XOR[c1]
                    b = XOR[c2] ^ XOR[c1]
                    c = XOR[0] ^ XOR[c2]
                else:
                    a = XOR[c1]
                    b = XOR[c2]
                    c = XOR[0] ^ XOR[c1] ^ XOR[c2]

                cur = max(a, b, c) - min(a, b, c)
                ans = min(cur, ans)

        return ans

s = Solution()
nums = [1,5,5,4,11]
edges = [[0,1],[1,2],[1,3],[3,4]]

nums = [5,5,2,4,4,2]
edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
print(s.minimumScore(nums, edges))




















































































