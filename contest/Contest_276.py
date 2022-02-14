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
#     def divideString(self, s: str, k: int, fill: str) -> List[str]:
#         n = len(s)
#         r = n % k
#         # print(r)
#         if r > 0:
#             s += fill * (k - r)
#         ans = [s[(i * k):(i + 1) * k] for i in range(len(s) // k)]
#         return ans
#
#
# ss = Solution()
# s = "abcdefghi"
# k = 1
# fill = "x"
# print(ss.divideString(s, k, fill))

# class Solution:
#     def minMoves(self, target: int, maxDoubles: int) -> int:
#         if target == 1:
#             return 0
#         ans = 0
#
#         while maxDoubles > 0 and target > 1:
#             if target % 2 == 1:
#                 target -= 1
#                 ans += 1
#             else:
#                 target //= 2
#                 maxDoubles -= 1
#                 ans += 1
#
#         ans += target - 1
#         return ans

# class Solution:
#     def mostPoints(self, questions: List[List[int]]) -> int:
#         n = len(questions)
#         dp = [0] * (n + 1)
#         dp[0] = 0
#         for i in range(0, n):
#             p, b = questions[i]
#             dp[i + 1] = max(dp[i + 1], dp[i])
#             if i + b + 1 < n:
#                 dp[i + b + 1] = max(dp[i + b + 1], dp[i] + p)
#         # print(dp)
#
#         ans = 0
#         for i in range(n):
#             ans = max(ans, dp[i] + questions[i][0])
#         return ans
#
# s = Solution()
# questions = [[3,2],[4,3],[4,4],[2,5]]
# print(s.mostPoints(questions))

class Solution:
    def maxRunTime(self, n: int, B: List[int]) -> int:
        b = len(B)
        B.sort()
        A = B[:(b - n)]
        B = B[(b - n):]

        # print(A)
        # print(B)

        ans = B[0]
        left = sum(A)

        for i in range(n - 1):
            diff = B[i + 1] - B[i]
            if left >= diff * (i + 1):
                left -= diff * (i + 1)
                ans += diff
            else:
                ans += left // (i + 1)
                left -= left // (i + 1)
                break
        else:
            ans += left // n
        return ans

s = Solution()
n = 3
B = [10,10,3,5]

# n = 12
# B = [11,89,16,32,70,67,35,35,31,24,41,29,6,53,78,83]

print(s.maxRunTime(n, B))
























































































