import collections
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
#     def cellsInRange(self, s: str) -> List[str]:
#         x1, x2, y1, y2 = s[0], s[3], int(s[1]), int(s[4])
#         ans = []
#         for j in range(ord(x1), ord(x2) + 1):
#             for i in range(y1, y2 + 1):
#
#                 ans.append(f'{chr(j)}{i}')
#         return ans




# class Solution:
#     def minimalKSum(self, nums: List[int], k: int) -> int:
#         ans = (1 + k) * k // 2
#         cur = k + 1
#         A = set(nums)
#         A = list(A)
#         A.sort()
#         C = collections.Counter(nums)
#         # print(A, C)
#         for a in A:
#             if a < cur:
#                 ans -= a
#                 ans += a * C[a]
#                 ans += cur
#                 cur += 1
#             else:
#                 ans += a * C[a]
#
#         return ans - sum(nums)
#
#
# nums = [1,4,25,10,25]
# k = 2
# s = Solution()
# print(s.minimalKSum(nums, k))


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        has_parent = set()
        tree = defaultdict(lambda : [None, None])
        for p, c, is_left in descriptions:
            has_parent.add(c)
            tree[p][1 - is_left] = c

        root_val = None
        for k in tree.keys():
            if k not in has_parent:
                root_val = k
                break

        def dfs(root_val):
            if root_val is None:
                return None
            return TreeNode(root_val, dfs(tree[root_val][0]), dfs(tree[root_val][1]))

        return dfs(root_val)

# class Solution:
#     def replaceNonCoprimes(self, A: List[int]) -> List[int]:
#         stack = []
#         for a in A:
#             while stack and gcd(a, stack[-1]) > 1:
#                 a = (a // gcd(a, stack[-1]) * stack[-1])
#                 stack.pop()
#             stack.append(a)
#         return stack
















