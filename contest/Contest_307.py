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


MOD = 1000000007

# class Solution:
#     def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
#         ans = 0
#         curEx = initialExperience
#         curEn = initialEnergy
#         n = len(energy)
#         for i in range(n):
#             en = energy[i]
#             ex = experience[i]
#             if curEn > en:
#                 curEn -= en
#             else:
#                 ans += en - curEn + 1
#                 curEn = 1
#
#             if curEx > ex:
#                 curEx += ex
#             else:
#                 ans += ex - curEx + 1
#                 curEx = ex * 2 + 1
#             # print(curEn, curEx)
#         return ans
#
# initialEnergy = 1
# initialExperience = 1
# energy = [1,1,1,1]
# experience = [1,1,1,50]
# s = Solution()
# print(s.minNumberOfHours(1,1,energy, experience))

class Solution:
    def largestPalindromic(self, num: str) -> str:
        C = collections.Counter(num)
        ans = ''
        for i in range(9, -1, -1):
            c = str(i)
            if c not in C:
                continue
            if c == '0' and not ans:
                break
            ans += c * (C[c] // 2)
        ex = ''
        for i in range(9, -1, -1):
            c = str(i)
            if c not in C:
                continue
            if C[c] % 2 == 1:
                ex = c
                break
        ans = ans + ex + ans[::-1]
        if ans == '':
            ans = '0'
        return ans
#
num = "444947137"
num = "00009"
num = "00"
s = Solution()
print(s.largestPalindromic(num))

# class Solution:
#     def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
#         startNode = None
#         nodes = {}

#         def visit(root, par):
#             if root == None:
#                 return

#             nonlocal startNode
#             if root.val == start:
#                 startNode = root

#             nodes[root] = (par, root.left, root.right)
#             visit(root.left, root)
#             visit(root.right, root)

#         visit(root, None)

#         V = set()
#         ans = 0

#         def dfs(cur, step):
#             nonlocal ans
#             if not cur:
#                 return

#             ans = max(ans, step)
#             for nxt in nodes[cur]:
#                 if nxt and nxt not in V:
#                     V.add(nxt)
#                     dfs(nxt, step + 1)
#         V.add(startNode)
#         dfs(startNode, 0)
#         return ans





















































































