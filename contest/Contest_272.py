from typing import *
from Tree import *

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, u):
        if u != self.parent.setdefault(u, u):
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            self.parent[pu] = pv


# class Solution:
#     def firstPalindrome(self, words: List[str]) -> str:
#         for w in words:
#             if w == w[::-1]:
#                 return w
#         return ""

# class Solution:
#     def addSpaces(self, s: str, spaces: List[int]) -> str:
#         ans = []
#         last = 0
#         for sp in spaces:
#             ans.append(s[last:sp])
#             ans.append(" ")
#             last = sp
#         ans.append(s[last:])
#         return "".join(ans)
#
# class Solution:
#     def getDescentPeriods(self, prices: List[int]) -> int:
#         dp = [1 for _ in range(len(prices))]
#         ans = 1
#         for i in range(1, len(prices)):
#             if prices[i] == prices[i-1] - 1:
#                 dp[i] = dp[i-1] + 1
#             ans += dp[i]
#         return ans


import bisect
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        ans = 0

        def dfs(A):
            nonlocal ans
            dp = []
            for a in A:
                if not dp or dp[-1] <= a:
                    dp.append(a)
                else:
                    i = bisect.bisect_right(dp, a)
                    # if dp[i] == a:
                    #     bisect.insort_left(dp, a)
                    # else:
                    dp[i] = a
            ans += len(A) - len(dp)

            print(dp)

        for i in range(k):
            dfs(arr[i::k])

        return ans

s = Solution()
arr = [5,4,3,2,1]
k = 1
arr = [4,1,5,2,6,2]
k = 2
arr = [2,2,2,2,2,1,1,4,4,3,3,3,3,3]
k = 1

print(s.kIncreasing(arr, k))