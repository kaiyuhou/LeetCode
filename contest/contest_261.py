from typing import *
from Tree import *

# class Solution:
#     def minimumMoves(self, s: str) -> int:
#         ans = 0
#         i = 0
#         while i < len(s):
#             if s[i] == 'X':
#                 i += 3
#                 ans += 1
#             i += 1
#         return ans
#
#
# s = Solution()

# class Solution:
#     def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
#         wait = mean * (n + len(rolls)) - sum(rolls)
#         if wait < n * 1 or wait > n * 6:
#             return []
#         wait -= n
#         ans = [1] * n
#         for i in range(n):
#             if wait > 0:
#                 ans[i] += min(5, wait)
#                 wait -= 5
#             else:
#                 break
#         return ans

import functools
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        n = len(stones)
        if n < 2:
            return False

        n0, n1, n2 = 0, 0, 0
        for s in stones:
            if s % 3 == 0:
                n0 += 1
            if s % 3 == 1:
                n1 += 1
            if s % 3 == 2:
                n2 += 1

        mem = {}

        def dfs(n0, n1, n2, re, turn):
            if n0 < 0 or n1 < 0 or n2 < 0:
                return True

            if n0 + n1 + n2 == 0:
                return turn == 1

            if (n0, n1, n2, re, turn) in mem:
                return mem[(n0, n1, n2, re, turn)]

            if re == 0:
                ans = dfs(n0, n1 - 1, n2, 1, 1 - turn) == False or dfs(n0, n1, n2 - 1, 2, 1 - turn) == False
            elif re == 1:
                ans = dfs(n0 - 1, n1, n2, 1, 1 - turn) == False or dfs(n0, n1 - 1, n2, 2, 1 - turn) == False
            else: # 2
                ans = dfs(n0 - 1, n1, n2, 2, 1 - turn) == False or dfs(n0, n1, n2 - 1, 1, 1 - turn) == False
            mem[(n0, n1, n2, re, turn)] = ans
            return ans

        # for n0 in range(7):
        #     for n1 in range(10):
        #         print('-')
        #         for n2 in range(10):
        #             print(f'{n0} {n1} {n2}: {dfs(n0, n1, n2, 0, 0)}')

        # if n0 == n or n1 == n or n2 == n:
        #     return False
        # if n0 == 0:
        #     return True
        if n0 % 2 == 0:
            if n1 == 0 or n2 == 0:
                return False
            return True
        if n0 % 2 == 1:
            if abs(n1 - n2) <= 2:
                return False
            return True


        # return dfs(n0, n1, n2, 0, 0)

s = Solution()
# stones = [2,1]
# stones = [1, 2, 1, 3]
stones = [5,1,2,4,3]

print(s.stoneGameIX(stones))







