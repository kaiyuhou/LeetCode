import collections
import heapq
from typing import *
from collections import *
from math import *
from itertools import *

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
#     def largestInteger(self, A: List[int], k: int) -> int:
#         dp = collections.Counter()
#         n = len(A)
#         for i in range(n - k + 1):
#             B = set()
#             for j in range(k):
#                 B.add(A[i + j])
#             for b in B:
#                 dp[b] += 1
        
#         ans = -1
#         for i, k in dp.items():
#             if k == 1 and i > ans:
#                 ans = i
#         return ans 

# class Solution:
#     def longestPalindromicSubsequence(self, s: str, k: int) -> int:
#         def cost(c1, c2):
#             dif = abs(ord(c1) - ord(c2))
#             return min(dif, 26 - dif)
        
#         @cache
#         def dp(i, j, k):
#             if i > j:
#                 return 0
#             if i == j:
#                 return 1

#             ans = max(dp(i, j - 1, k), dp(i + 1, j, k))
#             c = cost(s[i], s[j])
#             if c <= k:
#                 ans = max(ans, 2 + dp(i + 1, j - 1, k - c))
#             return ans

#         return dp(0, len(s) - 1, k)

class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int: 
        n = len(nums)
        pref = list(accumulate(nums, initial=0))

        @cache
        def dp(i, k, extendable):
            if n - i < k * m:
                return -inf
            if i == n:
                return 0 if k == 0 else -inf
            ans = dp(i + 1, k, False)
            if extendable:
                ans = max(ans, dp(i + 1, k, True) + nums[i])
            if k > 0 and i + m <= n:
                ans = max(ans, dp(i + m, k- 1, True) + pref[i + m] - pref[i])
            return ans
        return dp(0, k, False)
        








class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        if m == 1:
            nums.sort(reverse=True)
            return sum(nums[:k])

        ans = [float('-inf')] * (k + 1)
        ans[0] = 0
        dp = [[[float('-inf')] * 4 for _ in range(len(nums))] for _ in range(k + 1)] 
        # dp = [[[float('-inf')] * (m + 2) for _ in range(len(nums))] for _ in range(k + 1)] 
        
        dp[1][0][0] = nums[0]
        if m == 1:
            dp[1][0][1] = nums[0]
            ans[1] = nums[0]

        for pos in range(1, len(nums)):
            a = nums[pos]
            bb = (pos + 1) // m + 1
            bb = min(bb, k)
            for i in range(bb, 0, -1):
                dp[i][pos][0] = ans[i - 1] + a
                dp[i][pos][1] = dp[i][pos - 1][0] + a
                dp[i][pos][2] = dp[i][pos - 1][1] + a
                # for j in range(2, m + 1):
                #     dp[i][pos][j] = dp[i][pos - 1][j - 1] + a
                dp[i][pos][m] = max(dp[i][pos - 1][m - 1] + a, dp[i][pos - 1][m] + a)
                ans[i] = max(ans[i], dp[i][pos][m - 1], dp[i][pos][m])
        return ans[k]

# s = Solution()
# nums = [1,2,-1,3,3,4]
# k = 2
# m = 2

# # nums = [-10,3,-1,-2]
# # k = 4
# # m = 1

# # nums = [-8,1,-8,6,-9,5]
# # k = 1
# # m = 3

# print(s.maxSum(nums, k, m))
