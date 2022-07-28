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
#     def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
#         ans = []
#         n = len(nums)
#         last = 0
#         for i, a in enumerate(nums):
#             if a == key:
#                 for j in range(max(i - k, last), min(n, i + k + 1)):
#                     ans.append(j)
#                 last = j + 1
#         return ans

# class Solution:
#     def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
#         As = collections.defaultdict(int)
#         M = collections.defaultdict(int)
#
#         for i, (r1, c1, r2, c2) in enumerate(artifacts):
#             for x in range(r1, r2 + 1):
#                 for y in range(c1, c2 + 1):
#                     As[i] += 1
#                     M[x, y] = i
#         ans = 0
#         for x, y in dig:
#             if (x, y) in M.keys():
#                 i = M[x, y]
#                 As[i] -= 1
#                 if As[i] == 0:
#                     ans += 1
#         return ans

# class Solution:
#     def maximumTop(self, A: List[int], k: int) -> int:
#         n = len(A)
#         if k == 0:
#             return A[0]
#
#         if n == 1:
#             if k % 2 == 1:
#                 return -1
#             else:
#                 return A[0]
#
#         if k == 1:
#             return A[1]
#
#         if k < n:
#             ans = max(A[:k - 1])
#             ans = max(ans, A[k])
#             return ans
#
#         if k == n:
#             ans = max(A[:k - 1])
#             return ans
#
#         return max(A)

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        tos = defaultdict(list)
        froms = defaultdict(list)

        for f, t, w in edges:
            tos[f].append((t, w))
            froms[t].append((f, w))

        def dij(dist, queue, visited, G):
            while len(queue) > 0:
                d, cur = heapq.heappop(queue)
                if visited[cur]:
                    continue
                visited[cur] = True

                dist[cur] = d
                for neg, w in G[cur]:
                    if visited[neg]:
                        continue
                    if d + w < dist[neg]:
                        dist[neg] = d + w
                        heapq.heappush(queue, (d + w, neg))
            return dist

        dist_1 = [float('inf')] * n
        queue_1 = [(0, src1)]
        visited_1 = [False] * n
        dist_1 = dij(dist_1, queue_1, visited_1, tos)

        dist_2 = [float('inf')] * n
        queue_2 = [(0, src2)]
        visited_2 = [False] * n
        dist_2 = dij(dist_2, queue_2, visited_2, tos)

        dist_d = [float('inf')] * n
        queue_d = [(0, dest)]
        visited_d = [False] * n
        dist_d = dij(dist_d, queue_d, visited_d, froms)

        ans = float('inf')

        for i in range(n):
            if visited_1[i] and visited_2[i] and visited_d[i]:
                ans = min(ans, dist_1[i] + dist_2[i] + dist_d[i])

        if ans == float('inf'):
            return -1
        return ans

s = Solution()
n = 6
edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]
src1 = 0
src2 = 1
dest = 5
# Output: 9
print(s.minimumWeight(n, edges, src1, src2, dest))



































































