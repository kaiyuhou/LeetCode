from typing import *

# class Solution:
#     def judgePoint24(self, cards: List[int]) -> bool:
#         cards.sort()
#         ans = [False]
#         ops = [lambda a, b: a + b,
#                lambda a, b: a - b,
#                lambda a, b: b - a,
#                lambda a, b: a * b,
#                lambda a, b: a / b,
#                lambda a, b: b / a]
#         op0 = [ lambda a, b: a + b,
#                 lambda a, b: -(a + b),
#                 lambda a, b: 0]
#
#         checked = set()
#
#         def possible(a, b):
#             op_set = ops
#             if 0 in (a, b):
#                 op_set = op0
#             return (op(a, b) for op in op_set)
#
#         def dfs(remain):
#             if ans[0] == True or remain in checked:
#                 return
#             N = len(remain)
#
#             checked.add(remain)
#
#             if N == 2:
#                 for num in possible(remain[0], remain[1]):
#                     if abs(24 - num) < 0.0000001:
#                         ans[0] = True
#             else:
#                 for i in range(0, N - 1):
#                     for j in range(i + 1, N):
#                         for num in possible(remain[i], remain[j]):
#                             next_remain = list(remain[:i] + remain[i+1:j] + remain[j+1:] + (num,))
#                             next_remain.sort()
#                             # print(next_remain)
#                             dfs(tuple(next_remain))
#
#         cards.sort()
#         dfs(tuple(cards))
#         return ans[0]
#
# s = Solution()
# cards = [4,1,8,7]
# cards = [1,2,1,2]
# cards = [3,3,8,8]
# print(s.judgePoint24(cards))

import math
import itertools

class Solution:
    def judgePoint24(self, nums):
        if len(nums) == 1:
            return math.isclose(nums[0], 24)

        return any(
            self.judgePoint24([x] + rest)
            for a, b, *rest in itertools.permutations(nums)
            for x in {a + b, a - b, a * b, b and a / b}
        )

s = Solution()
cards = [4,1,8,7]
cards = [1,2,1,2]
cards = [3,3,8,8]
print(s.judgePoint24(cards))