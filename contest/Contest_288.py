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
#     def largestInteger(self, num: int) -> int:
#         s = list(str(num))
#         is_even = []
#         even = []
#         odd = []
#         for i, c in enumerate(s):
#             if int(c) % 2 == 0:
#                 is_even.append(True)
#                 even.append(c)
#             else:
#                 is_even.append(False)
#                 odd.append(c)
#
#         even.sort()
#         odd.sort()
#         ans = []
#
#         # print(is_even)
#
#         for f in is_even:
#             if f:
#                 ans.append(even.pop())
#             else:
#                 ans.append(odd.pop())
#         return int(''.join(ans))
#
# s = Solution()
# num = 1111
# print(s.largestInteger(num))

# class Solution:
#     def minimizeResult(self, expression: str) -> str:
#         a, b = expression.split('+')
#         ans = int(a) + int(b)
#         best = (0, len(b))
#         for i in range(len(a)):
#             for j in range(1, len(b) + 1):
#                 a1 = a[:i]
#                 a2 = a[i:]
#                 b1 = b[:j]
#                 b2 = b[j:]
#                 if not a1:
#                     a1 = 1
#                 if not b2:
#                     b2 = 1
#
#                 cur = int(a1) * (int(a2) + int(b1)) * int(b2)
#                 if cur < ans:
#                     ans = cur
#                     best = (i, j)
#
#         return f'{a[:best[0]]}({a[best[0]:]}+{b[:best[1]:]}){b[best[1]:]}'
#
# s = Solution()
# expression = "247+38"
# print(s.minimizeResult(expression))

# class Solution:
#     def maximumProduct(self, A: List[int], k: int) -> int:
#         if len(A) == 1:
#             return A[0] + k
#
#         A.sort()
#         last = A[0]
#         stop_tag = len(A)
#         for i in range(1, len(A)):
#             if A[i] == last:
#                 continue
#             else:
#                 if (A[i] - last) * i <= k:
#                     k -= (A[i] - last) * i
#                     last = A[i]
#                 else:
#                     stop_tag = i
#                     break
#
#         mod = 1000000007
#         ans = 1
#
#         # print(stop_tag)
#
#         plus = k // stop_tag
#         extra_n = k % stop_tag
#         for i in range(stop_tag):
#             if i < extra_n:
#                 ans = (ans * (last + plus + 1)) % mod
#             else:
#                 ans = (ans * (last + plus)) % mod
#
#         for i in range(stop_tag, len(A)):
#             ans = (ans * A[i]) % mod
#
#         return ans
#
#
# s = Solution()
# nums = [0,4]
# k = 5
# nums = [6]
# k = 2
# nums = [9,7,8]
# k = 9  # 1331
# print(s.maximumProduct(nums, k))
#

import bisect
class Solution:
    def maximumBeauty(self, F: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        F.sort()
        A = []
        for f in F:
            if f < target:
                A.append(f)
            else:
                break
        base_ans = (len(F) - len(A)) * full

        # print('base_ans: ', base_ans)

        n = len(A)
        if n == 0:
            return base_ans

        need_to_full = [0]
        for i in range(n - 1, -1, -1):
            need_to_full.append(need_to_full[-1] + (target - A[i]))
        # print('need_to_full: ', need_to_full)

        can_full = min(n, bisect.bisect(need_to_full, newFlowers) - 1)
        best = can_full * full
        # print("can_full best: ", best)

        used = 0
        last = A[0]
        cur = last * partial + min(n - 1, bisect.bisect(need_to_full, newFlowers) - 1) * full
        # print('init cur: ', cur)

        best = max(best, cur)
        for i in range(1, n):
            if A[i] == last:
                continue
            while last < A[i]:
                if newFlowers - used >= i:
                    last += 1
                    used += i
                    can_full_n = bisect.bisect(need_to_full, newFlowers - used) - 1
                    if can_full_n <= n - i:
                        cur = last * partial + can_full_n * full
                    else:
                        to_here_used = need_to_full[n - i]
                        rest = newFlowers - used - to_here_used
                        can_full_rest = rest // (target - last)
                        total_full = min(n - 1, can_full_rest + (n - i))
                        cur = last * partial + total_full * full

                    # print('cur with last: ', last, used, cur)
                    best = max(best, cur)
                else:
                    break
            if newFlowers - used < i:
                break

        if newFlowers - used >= n:
            while last < (target - 1):
                if newFlowers - used >= n:
                    last += 1
                    used += n
                    cur = last * partial
                    rest = newFlowers - used
                    can_full_rest = rest // (target - last)
                    total_full = min(n - 1, can_full_rest)
                    cur += total_full * full

                    # print('last_cur: ', cur)
                    best = max(best, cur)
                else:
                    break

        return base_ans + best

s = Solution()
flowers = [1,3,1,1]
newFlowers = 7
target = 6
full = 12
partial = 1
# flowers = [2,4,5,3]
# newFlowers = 10
# target = 5
# full = 2
# partial = 6
flowers = [18,16,10,10,5,1]
newFlowers = 10
target = 3
full = 15
partial = 4
flowers = [5,5,15,1,9]
newFlowers = 36
target = 12
full = 9
partial = 2
print(s.maximumBeauty(flowers, newFlowers, target, full, partial))



























































































