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
#     def answerQueries(self, A: List[int], queries: List[int]) -> List[int]:
#         A.sort()
#         ans = []
#         for q in queries:
#             cur = 0
#             cas = 0
#             for a in A:
#                 if cur + a > q:
#                     break
#                 cur += a
#                 cas += 1
#             ans.append(cas)
#         return ans

# class Solution:
#     def removeStars(self, s: str) -> str:
#         ans = []
#         for c in s:
#             if c == '*':
#                 ans.pop(-1)
#             else:
#                 ans.append(c)
#         return "".join(ans)

# class Solution:
#     def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
#         n = len(garbage)
#         G = [collections.Counter(g) for g in garbage]
#         ans = 0
#         travel.append(0)
#         for t in ('M', 'P', 'G'):
#             last_travel = 0
#             for i in range(n):
#                 if t in G[i]:
#                     ans += G[i][t]
#                     ans += last_travel
#                     last_travel = 0
#                 last_travel += travel[i]
#         return ans


class Solution:
    def buildMatrix(self, k: int, rowC: List[List[int]], colC: List[List[int]]) -> List[List[int]]:
        def get_order(C):
            order = []
            above_me_cnt = [0] * (k + 1)
            my_next = [[] for _ in range(k + 1)]
            for a, b in C:
                my_next[a].append(b)
                above_me_cnt[b] += 1

            stack = []
            for i in range(1, k + 1):
                if above_me_cnt[i] == 0:
                    stack.append(i)

            # print(my_next)
            # print(stack)
            # print(above_me_cnt)

            while stack:
                cur = stack.pop(0)
                order.append(cur)
                for nxt in my_next[cur]:
                    above_me_cnt[nxt] -= 1
                    if above_me_cnt[nxt] == 0:
                        stack.append(nxt)
            #     print(stack)

            # print(above_me_cnt)

            
            for abc in above_me_cnt:
                if abc > 0:
                    return None

            used = set(order)
            for i in range(1, k + 1):
                if i not in used:
                    order.append(i)

            ret = [0] * (k + 1)
            for i, a in enumerate(order):
                ret[a] = i

            # [0,3,1,2,0] means number 1 is the pos 3, number 2 is pos 1
            return ret

        row_order = get_order(rowC)
        col_order = get_order(colC)

        if row_order is None or col_order is None:
            return []

        ans = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            ans[row_order[i]][col_order[i]] = i
        return ans


k = 3
rowC = [[1,2],[3,2]]
colC = [[2,1],[3,2]]
s = Solution()
print(s.buildMatrix(k, rowC, colC))
