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
#     def countOperations(self, num1: int, num2: int) -> int:
#         ans = 0
#         while num1 != 0 and num2 != 0:
#             if num1 >= num2:
#                 num1 -= num2
#             else:
#                 num2 -= num1
#             ans += 1
#         return ans

# import collections
#
# class Solution:
#     def minimumOperations(self, nums: List[int]) -> int:
#         A = nums[::2]
#         B = nums[1::2]
#
#         AC = collections.Counter(A)
#         BC = collections.Counter(B)
#
#         nA = len(A)
#         nB = len(B)
#
#         ans = 1e6
#         for ak, av in AC.most_common(4):
#             for bk, bv in BC.most_common(4):
#                 if ak != bk:
#                     cur = (nA - av) + (nB - bv)
#                     ans = min(ans, cur)
#         if ans == 1e6:
#             ans = min(nA, nB)
#
#         return ans



# class Solution:
#     def minimumRemoval(self, A: List[int]) -> int:
#         A.sort()
#         ans = sum(A)
#         S = sum(A)
#         n = len(A)
#         acc = 0
#         for i, a in enumerate(A):
#             rest = n - i - 1
#             cur = acc + (S - acc - a - rest * a)
#             ans = min(cur, ans)
#             acc += a
#         return ans
#
# import collections
#
# class Solution:
#     def maximumANDSum(self, A: List[int], numSlots: int) -> int:
#         C = collections.Counter(A)
#         ans = 0
#         slots = collections.Counter()
#         big_slot = []
#         slot_nums = {}
#         for slot in range(1, numSlots + 1):
#             slot_nums[slot] = {}
#             for j in range(0, slot + 1):
#                 slot_nums[slot][j] = []
#
#         best_slot = {}
#         for i in range(1, 16):
#             cur = []
#             for slot in range(1, numSlots + 1):
#                 cur.append((i & slot, slot))
#                 big_slot.append((i & slot, slot, i))  # a & slot, slot, nums
#                 slot_nums[slot][i & slot].append(i)
#             cur.sort(reverse=True)
#             best_slot[i] = cur
#             print(i, cur)
#         big_slot.sort(reverse=True)
#         print(big_slot)
#         print(C)
#         print(slot_nums)
#
#         for i in range(numSlots):
#             while C[i] > 0 and slots[i] < 2:
#                 ans += i
#                 C[i] -= 1
#                 slots[i] += 1
#
#         for big, slot, num in big_slot:
#             if C[num] > 0 and slots[slot] < 2:
#                 cur_num = num
#                 for other in slot_nums[slot][big]:
#                     if C[other] > 0:
#                         cur_num = other
#                 C[cur_num] -= 1
#                 slots[slot] += 1
#                 ans += big
#
#             if C[num] > 0 and slots[slot] < 2:
#                 cur_num = num
#                 for other in slot_nums[slot][big]:
#                     if C[other] > 0:
#                         cur_num = other
#                 C[cur_num] -= 1
#                 slots[slot] += 1
#                 ans += big
#
#         return ans



        #
        # for i in range(1, 16):
        #     rest = C[i]
        #     while rest > 0:
        #         for k, v in best_slot[i]:
        #             if slots[v] < 2:
        #                 slots[v] += 1
        #                 ans += k
        #                 rest -= 1
        #                 print(i, v)
        #                 break
        # return ans


from functools import lru_cache

class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        @lru_cache(None)
        def dp(i, mask):
            if i >= len(nums):
                return 0
            ans = 0
            for slot in range(numSlots):
                if mask & (1 << slot * 2) == 0 or mask & (1 << (slot * 2 + 1)) == 0:
                    if mask & (1 << slot * 2) == 0:
                        new_mask = mask | (1 << slot * 2)
                    else:
                        new_mask = mask | (1 << (slot * 2 + 1))
                    ans = max(ans, dp(i + 1, new_mask) + ((slot + 1) & nums[i]))
            return ans
        return dp(0, 0)


# class Solution:
#     def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
#
#         @lru_cache(None)
#         def fn(k, m):
#             """Return max AND sum."""
#             if k == len(nums): return 0
#             ans = 0
#             for i in range(numSlots):
#                 if m & 1<<2*i == 0 or m & 1<<2*i+1 == 0:
#                     if m & 1<<2*i == 0: mm = m ^ 1<<2*i
#                     else: mm = m ^ 1<<2*i+1
#                     ans = max(ans, (nums[k] & i+1) + fn(k+1, mm))
#             return ans
#
#         return fn(0, 0)

s = Solution()
nums = [1,2,3,4,5,6] * 3
numSlots = 9
# nums = [1,3,10,4,7,1]
# numSlots = 9

# nums = [14,7,9,8,2,4,11,1,9]
# numSlots = 8
# # nums = [4,2,2,11,7,12,9,8]
# # numSlots = 4
#
# nums = [15,13,4,4,11,6,6,12,15,7,3,12,13,7]
# numSlots = 8

print(s.maximumANDSum(nums, numSlots))






















