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
#     def countElements(self, nums: List[int]) -> int:
#         nums.sort()
#         ans = 0
#         for a in nums:
#             if a > nums[0] and a < nums[-1]:
#                 ans += 1
#         return ans

# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
#         pos, neg = [], []
#         for a in nums:
#             if a < 0:
#                 neg.append(a)
#             else:
#                 pos.append(a)
#
#         ans = []
#         for i in range(len(pos)):
#             ans.append(pos[i])
#             ans.append(neg[i])
#         return ans

# class Solution:
#     def findLonely(self, nums: List[int]) -> List[int]:
#         nums.sort()
#         ans = []
#         n = len(nums)
#         for i in range(n):
#             if i > 0:
#                 if nums[i-1] in (nums[i], nums[i] + 1, nums[i] - 1):
#                     continue
#             if i < n - 1:
#                 if nums[i + 1] in (nums[i], nums[i] + 1, nums[i] - 1):
#                     continue
#             ans.append(nums[i])
#         return ans

import itertools
class Solution:
    def maximumGood(self, S: List[List[int]]) -> int:
        n = len(S)
        ps = tuple([i for i in range(n)])
        for i in range(n, 0, -1):
            for pc in itertools.combinations(ps, i):
                # print(pc)
                for p1, p2 in itertools.product(pc, ps):
                    if S[p1][p2] == 0 and p2 in pc:
                        break
                    if S[p1][p2] == 1 and p2 not in pc:
                        break
                else:
                    # print(pc)
                    return i
        return 0


s = Solution()
# statements = [[2,1,2],[1,2,2],[2,0,2]]
statements = [[1] * 15 for _ in range(15)]
# statements = [[2,2,2,2],[1,2,1,0],[0,2,2,2],[0,0,0,2]]
statements = [[2,0,0,2,2,0,1,2],[0,2,1,0,0,1,1,0],[0,0,2,0,2,0,1,2],[1,0,2,2,1,0,0,1],[1,1,2,1,2,2,1,0],[2,0,0,0,1,2,0,0],[0,2,2,0,2,1,2,0],[2,1,2,0,0,1,0,2]]
print(s.maximumGood(statements))












