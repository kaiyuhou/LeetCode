import collections
import heapq
from typing import *
from collections import *
# from math import *

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
#     def isPossibleToSplit(self, nums: List[int]) -> bool:
#         C = collections.Counter()
#         for a in nums:
#             C[a] += 1
#             if C[a] > 2:
#                 return False
#         return True

# class Solution:
#     def largestSquareArea(self, A: List[List[int]], B: List[List[int]]) -> int:
#         def ix(a0, a1, b0, b1):
#             if a1 > b1:
#                 return ix(b0, b1, a0, a1)
            
#             if a0 > b0:
#                 return a1 - a0
#             return a1 - b0
                 
#         n = len(A)
#         ans = 0
#         for i in range(n):
#             for j in range(n):
#                 if i == j:
#                     continue
#                 x = ix(A[i][0], B[i][0], A[j][0],B[j][0])
#                 y = ix(A[i][1], B[i][1], A[j][1],B[j][1])
#                 if x > 0 and y > 0:
#                     ans = max(ans, min(x * x, y * y))        
#         return ans

# s = Solution()
# A = [[1,1],[2,2],[3,1]]
# B = [[3,3],[4,4],[6,6]]
# print(s.largestSquareArea(A, B))

# import functools
# class Solution:
#     def earliestSecondToMarkIndices(self, A: List[int], CI: List[int]) -> int:
#         n = len(A)
#         m = len(CI)

#         if sum(A) + n > m:
#             return -1

#         ans = [m + 1]

#         @functools.lru_cache(None)
#         def dfs(cur_idx, space, V):
#             V = set(V)
#             visited = sum(V)

#             if cur_idx > m:
#                 return 

#             cur_ci = CI[cur_idx - 1]
#             cur_va = A[cur_ci - 1]

#             if V[cur_ci] == True:
#                 dfs(cur_idx + 1, space + 1, tuple(V))
#                 return
            
#             if space >= cur_va:
#                 if visited + 1 == n:
#                     ans[0] = min(ans[0], cur_idx)
#                     return

#                 V.add(cur_ci)
#                 dfs(cur_idx + 1, space - cur_va, tuple(V))
#                 V.remove(cur_ci)
                
#             dfs(cur_idx + 1, space + 1, tuple(V))

#         V = set()
#         dfs(1, 0, tuple(V))
#         if ans[0] == m + 1:
#             return -1
#         return ans[0]


# import functools
# class Solution:
#     def earliestSecondToMarkIndices(self, A: List[int], CI: List[int]) -> int:
#         n = len(A)
#         m = len(CI)

#         S = sum(A) + n

#         ans = m + 1
#         for i in range(m, S - 1, -1):
#             B = [a for a in A]
#             todo = []
#             todo_idx = 0
#             V = set()
#             for j in range(i, 0, -1):
#                 cur_idx = CI[j - 1] - 1
#                 if cur_idx not in V:
#                     V.add(cur_idx)
#                     todo.append(cur_idx)
#                 else:
#                     while todo_idx < len(todo) and B[todo[todo_idx]] == 0:
#                         todo_idx += 1
#                     if todo_idx >= len(todo):
#                         continue
#                     B[todo[todo_idx]] -= 1
#             if len(V) == n and sum(B) == 0:
#                 ans = i
#         if ans == m + 1:
#             return -1
#         return ans

# s = Solution()
# A = [2,2,0]
# CI = [2,2,2,2,3,2,2,1]
# A = [0,3,3]
# CI = [3,2,1,1,3,2,3,3,3]
# A = [1,3,13,4,7,8,3,1,1]
# CI = [9,8,4,3,9,5,6,7,9,4,7,9,7,5,4,7,9,6,3,7,3,3,8,8,9,3,6,2,3,9,4,6,1,5,3,9,5,3,5,3,2,8,4,2,3,7,9,5,8,7,3,4,3,5,6,8,9,8,3,2,6]
# print(s.earliestSecondToMarkIndices(A, CI))        

from collections import Counter
import heapq

# class Solution:
#     def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
#         for i in range(len(changeIndices)):
#             changeIndices[i] -= 1

#         def can_mark(maximum_time):
#             first_time_to_zero_num = [MOD for i in range(nums)]
#             for i in range(len(changeIndices)):
#                 num_index = changeIndices[]





















