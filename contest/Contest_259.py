from typing import *
from Tree import *

from collections import Counter

# class Solution:
#     def finalValueAfterOperations(self, operations: List[str]) -> int:
#         c = Counter(operations)
#         return c['++X'] + c["X++"] - c["--X"] - c["X--"]

# class Solution:
#     def sumOfBeauties(self, nums: List[int]) -> int:
#         n = len(nums)
#         leftB = [0] * n
#         rightB = [10**6] * n
#         for i in range(1, n):
#             leftB[i] = max(leftB[i - 1], nums[i - 1])
#         for i in range(n-2, -1, -1):
#             rightB[i] = min(rightB[i + 1], nums[i + 1])
#
#         # print(leftB, rightB)
#
#         ans = 0
#         for i in range(1, n-1):
#             if leftB[i] < nums[i] < rightB[i]:
#                 ans += 2
#             elif nums[i-1] < nums[i] < nums[i+1]:
#                 ans += 1
#
#         return ans
#
# s = Solution()
# # nums = [1,2,3]
# # nums = [2,4,6,4]
# nums = [3,2,1]
# nums = [1,2,3,4,5,9]
# print(s.sumOfBeauties(nums))

class DetectSquares:

    def __init__(self):
        self.p = Counter()
        self.xs = {}

    def add(self, point: List[int]) -> None:
        x, y = point
        if x not in self.xs:
            self.xs[x] = set()
        self.xs[x].add(y)
        self.p[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        cx, cy = point
        if cx not in self.xs:
            return 0
        ans = 0
        for y in self.xs[cx]:
            if y == cy:
                continue
            dis = abs(y - cy)
            ans += self.p[(cx, y)] * self.p[cx - dis, y] * self.p[cx - dis, cy]
            ans += self.p[(cx, y)] * self.p[cx + dis, y] * self.p[cx + dis, cy]
        return ans


