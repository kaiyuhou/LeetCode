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
#     def fillCups(self, A: List[int]) -> int:
#         ans = 0
#         A.sort()
#         while A[2] > 0:
#             ans += 1
#             A[1] -= 1
#             A[2] -= 1
#             A.sort()
#         return ans


# class SmallestInfiniteSet:
#
#     def __init__(self):
#         self.dp = [True] * 1001
#         self.dp[0] = False
#
#     def popSmallest(self) -> int:
#         for i in range(1001):
#             if self.dp[i]:
#                 self.dp[i] = False
#                 return i
#
#     def addBack(self, num: int) -> None:
#         if num <= 1000:
#             self.dp[num] = True


# class Solution:
#     def canChange(self, A: str, B: str) -> bool:
#         n = len(A)
#         As = []
#         Bs = []
#         for i in range(n):
#             if A[i] != '_':
#                 As.append(A[i])
#             if B[i] != '_':
#                 Bs.append(B[i])
#         if As != Bs:
#             return False
#         A = list(A)
#
#
#         i = 0
#         j = 0
#         Arest = 0
#         Brest = 0
#         while i < n and j < n:
#             # print(i, j)
#             # print(A[i], B[j])
#             if A[i] == B[j]:
#                 i += 1
#                 j += 1
#                 # if A[i] != '_':
#                 #     k += 1
#                 continue
#             if B[j] == '_' and Arest > 0:
#                 Arest -= 1
#                 j += 1
#                 continue
#             if A[i] == '_' and Brest > 0:
#                 Brest -= 1
#                 i += 1
#                 continue
#
#             if B[j] == 'L':
#                 while A[i] != 'L':
#                     i += 1
#                     Arest += 1
#                 i += 1
#                 j += 1
#                 continue
#             if A[i] == 'R':
#                 while B[j] != 'R':
#                     j += 1
#                     Brest += 1
#                 i += 1
#                 j += 1
#                 continue
#             # print(i, j)
#             return False
#         return True
#
# s = Solution()
# start = "_L__R__R_"
# target = "L______RR"
# start = "R_L_"
# target = "__LR"
# start = "_R"
# target = "R_"
# print(s.canChange(start, target))

from collections import Counter
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 1000000007

        nxt = {i: [] for i in range(1, maxValue + 1)}
        for i in range(1, maxValue + 1):
            cur = i
            while cur <= maxValue:
                nxt[i].append(cur)
                cur += i

        dp = Counter([i for i in range(1, maxValue + 1)])
        for i in range(n - 1):
            new_dp = Counter()
            for k, v in dp.items():
                for step in nxt[k]:
                    new_dp[step] += v
                    new_dp[step] %= MOD
            dp = new_dp
        return sum(dp.values()) % MOD

s = Solution()
n = 2
maxValue = 5
n = 5
maxValue = 3
n = 1000
maxValue = 1000
print(s.idealArrays(n, maxValue))













































































































