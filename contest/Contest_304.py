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
#     def minimumOperations(self, nums: List[int]) -> int:
#         ans = 0
#         A = [a for a in nums if a > 0]
#         while A and max(nums) > 0:
#             cur = min(A)
#             A = [a - cur for a in A if a - cur > 0 ]
#             ans += 1
#         return ans


# class Solution:
#     def maximumGroups(self, A: List[int]) -> int:
#         n = len(A)
#         ans = 0
#         while n > ans:
#             ans += 1
#             n -= ans
#         return ans



# class Solution:
#     def closestMeetingNode(self, E: List[int], node1: int, node2: int) -> int:
#         n = len(E)
#         step1 = [-1] * n
#         cur_step = 0
#         cur = node1
#         while cur != -1 and step1[cur] == -1:
#             step1[cur] = cur_step
#             cur_step += 1
#             cur = E[cur]
#
#         step2 = [-1] * n
#         cur_step = 0
#         cur = node2
#         while cur != -1 and step2[cur] == -1:
#             step2[cur] = cur_step
#             cur_step += 1
#             cur = E[cur]
#
#         ans = -1
#         best = n + 1
#         for i in range(n):
#             if step1[i] != -1 and step2[i] != -1:
#                 cur_best = max(step1[i], step2[i])
#                 if cur_best < best:
#                     ans = i
#                     best = cur_best
#                 elif cur_best == best:
#                     ans = min(ans, i)
#
#         return ans
#
#         #
#         #
#         #
#         #
#         #
#         #
#         #
#         # # ans1, ans1_len = -1, n + 1
#         # # if step1[node2] != -1:
#         # #     ans1 = node2
#         # #     ans1_len = step1[node2]
#         # #
#         # # print(step1, ans1, ans1_len)
#         # #
#         # #
#         # # cur_step = 1
#         # # cur = E[node2]
#         # # V = [False] * n
#         # # while cur != -1 and V[cur] == False:
#         # #     if step1[cur] != -1:
#         # #         ans2_len = max(cur_step, step1[cur])
#         # #         if ans2_len < ans1_len:
#         # #             return cur
#         # #         elif ans2_len == ans1_len:
#         # #             return min(cur, ans1)
#         # #         else:
#         # #             return ans1
#         # #     V[cur] = True
#         # #     cur = E[cur]
#         # #     cur_step += 1
#         # return ans1
#
# s = Solution()
# edges = [1,2,3,4,5,0]
# node1 = 3
# node2 = 0
# print(s.closestMeetingNode(edges, node1, node2))


class Solution:
    def longestCycle(self, E: List[int]) -> int:
        n = len(E)
        V = [False] * n
        MyTurn = [-1] * n
        Step = [-1] * n
        ans = -1
        for i in range(n):
            if V[i]:
                continue
            cur = i
            step = 0
            while cur != -1:
                if V[cur]:
                    if MyTurn[cur] != i:
                        break
                    else:
                        cur_ans = step - Step[cur]
                        ans = max(ans, cur_ans)
                        break
                Step[cur] = step
                MyTurn[cur] = i
                V[cur] = True
                step += 1
                cur = E[cur]
        return ans




































































