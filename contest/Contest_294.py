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
#     def percentageLetter(self, s: str, letter: str) -> int:
#         if letter not in s:
#             return 0
#         C = collections.Counter(s)
#         c = C[letter]
#         n = len(s)
#         return int(c * 100 / n)

# class Solution:
#     def maximumBags(self, C: List[int], R: List[int], aR: int) -> int:
#         n = len(C)
#         A = [C[i] - R[i] for i in range(n)]
#         A.sort()
#         ans = 0
#         for a in A:
#             if aR < a:
#                 break
#             aR -= a
#             ans += 1
#         return ans

# class Solution:
#     def minimumLines(self, stockPrices: List[List[int]]) -> int:
#         A = []
#         for d, p in stockPrices:
#             A.append((d, p))
#         A.sort()
#         n = len(A)
#         if n == 1:
#             return 0
#         ans = 1
#         x = (A[1][0] - A[0][0])
#         y = (A[1][1] - A[0][1])
#         # print(x)
#         for i in range(2, n):
#             cur_x = (A[i][0] - A[i - 1][0])
#             cur_y = (A[i][1] - A[i - 1][1])
#             if x * cur_y == y * cur_x:
#                 continue
#             else:
#                 ans += 1
#                 x = cur_x
#                 y = cur_y
#         return ans
#
# s = Solution()
# sp = [[1,1000000000],[1000000000,1000000000],[999999999,1],[2,999999999]]
# print(s.minimumLines(sp))

class Solution:
    def totalStrength(self, A: List[int]) -> int:
        print("call")
        MOD = 1000000007
        n = len(A)

        APDX = [0]
        for a in A:
            APDX.append(APDX[-1] + a)
        # print(APDX)

        TR = [0]
        for i, a in enumerate(A):
            TR.append((TR[-1] + a * (i + 1)) % MOD )

        ans = A[0] * A[0]
        dp = ans
        to_min = [A[0]]
        sum_min = A[0]

        for i in range(1, n):
            a = A[i]
            extra_sum = 0

            R = 0
            prefix = 0

            keep_index = i - 1
            while keep_index >= 0:
                if to_min[keep_index] <= a:
                    break
                else:
                    prefix += A[keep_index]
                    R += prefix * to_min[keep_index]
                    R %= MOD
                    extra_sum += to_min[keep_index]
                    to_min[keep_index] = a
                    keep_index -= 1

            R_len = i - keep_index
            L = dp - R
            new_L = L + (sum_min - extra_sum) * a

            tr = TR[i] - TR[keep_index]
            r_sum = APDX[i + 1] - APDX[keep_index]
            tr -= (keep_index + 1) * r_sum
            new_R = tr * a

            # eventually
            new_dp = new_L + new_R
            new_dp %= MOD
            ans += new_dp
            ans %= MOD
            to_min.append(a)
            sum_min = sum_min - extra_sum + R_len * a

        print("OK")
        return ans

s = Solution()
strength = [1,3,1,2]
ans = s.totalStrength(strength)
print(ans)
































s  = Solution()
A = [1,3,1,2]
print(s.totalStrength(A))






























