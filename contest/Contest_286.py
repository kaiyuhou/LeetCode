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
#     def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
#         C1 = collections.Counter(nums1)
#         C2 = collections.Counter(nums2)
#
#         ans = [[], []]
#         for key in C1.keys():
#             if key not in C2:
#                 ans[0].append(key)
#
#         for key in C2.keys():
#             if key not in C1:
#                 ans[1].append(key)
#
#         return ans


# class Solution:
#     def minDeletion(self, nums: List[int]) -> int:
#         ans = 0
#         last = None
#         i = 0
#         for a in nums:
#             if i % 2 == 0:
#                 i += 1
#                 last = a
#             else:
#                 if a == last:
#                     ans += 1
#                 else:
#                     i += 1
#         if i % 2 == 1:
#             ans += 1
#         return ans


# class Solution:
#     def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
#         ans = []
#         size = (intLength + 1) // 2
#         is_even = (intLength % 2 == 0)
#         for q in queries:
#             base = 10 ** (size - 1) - 1
#             num = base + q
#             if is_even:
#                 cur = str(num) + str(num)[::-1]
#             else:
#                 cur = str(num) + str(num)[-2::-1]
#             if len(cur) != intLength:
#                 ans.append(-1)
#             else:
#                 ans.append(int(cur))
#         return ans
#
#
# s = Solution()
# queries = [1,2,3,4,5,90]
# intLength = 3
# queries = [1,2,3]
# intLength = 2
# queries = [2,201429812,8,520498110,492711727,339882032,462074369,9,7,6]
# intLength =1
# print(s.kthPalindrome(queries, intLength))

import heapq

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        dp = collections.defaultdict(int)
        for p in piles:
            n = len(p)
            a = [0] * n
            for i in range(n):
                a[i] = a[i - 1] + p[i]

            for i in range(k, 0, -1):
                best = dp[i]
                for j in range(n):
                    if i - (j + 1) < 0:
                        break
                    if dp[i - (j + 1)] + a[j] > best:
                        best = dp[i - (j + 1)] + a[j]
                dp[i] = best

        return dp[k]


        #
        #
        #
        #
        # while n > 0:
        #     for j in range(n, k + 1):
        #         dp[j] = max(dp[j], dp[j - n] + tot)
        #     tot -= p[n - 1]
        #     n -= 1
        #     print(n)
        #     print(dp)

        # print(dp)


s = Solution()
piles = [[1,100,3],[7,8,9]]
k = 2
# piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]]
# k = 7

piles = [[37,88],[51,64,65,20,95,30,26],[9,62,20],[44]]
k = 9

# piles = [[200], [200], [200], [1,1,1,300]]
# k = 4

# piles = [[48,14,23,38,33,79,3,52,73,58,49,23,74,44,69,76,83,41,46,32,28]]
# k = 10  # 421

print(s.maxValueOfCoins(piles, k))
























# cur_ans = 0
# cur_tot = 0
# aves = []
# q = []
#
# for i, p in enumerate(piles):
#     n = min(len(p), k)
#     tot = 0
#     aves.append([])
#     for j in range(n):
#         tot += p[j]
#         aves[i].append(tot / (j + 1))
#     cur_ans += tot
#     cur_tot += n
#     q.append((aves[i][j], piles[i][j], i, j))
#
# def get_small_ave(q):
#     ans_s = q[0][0]
#     ans_i = q[0][2]
#     ans_j = q[0][3]
#     for s, _, i, j in q:
#         if j < 0:
#             continue
#         if s < ans_s:
#             ans_s, ans_i, ans_j = s, i, j
#     return ans_s, ans_i, ans_j
#
# def get_small_last(q):
#     ans_s = q[0][1]
#     ans_i = q[0][2]
#     ans_j = q[0][3]
#     for _, s, i, j in q:
#         if j < 0:
#             continue
#         if s < ans_s:
#             ans_s, ans_i, ans_j = s, i, j
#     return ans_s, ans_i, ans_j
#
# while cur_tot > k:
#     ave_s, ave_i, ave_j = get_small_ave(q)
#     last_s, last_i, last_j = get_small_last(q)
#     cur_tot -= 1
#
#     if last_s < ave_s:
#         cur_ans -= last_s
#         last_j -= 1
#         if last_j >= 0:
#             q[last_i] = (aves[last_i][last_j], piles[last_i][last_j], last_i, last_j)
#         else:
#             q[last_i] = (float('inf'), float('inf'), last_i, last_j)
#     else:
#         cur_ans -= piles[ave_i][ave_j]
#         ave_j -= 1
#         if ave_j >= 0:
#             q[ave_i] = (aves[ave_i][ave_j], piles[ave_i][ave_j], ave_i, ave_j)
#         else:
#             q[ave_i] = (float('inf'), float('inf'), ave_i, ave_j)
#
# print(q)




















