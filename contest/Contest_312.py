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
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#         A = []
#         for i in range(len(names)):
#             A.append((heights[i], names[i]))
#         A.sort(reverse=True)
#         ans = [a[1] for a in A]
#         return ans

# class Solution:
#     def longestSubarray(self, A: List[int]) -> int:
#         k = max(A)
#         ans = 1
#         cur = 0
#         for a in A:
#             if a == k:
#                 cur += 1
#                 ans = max(ans, cur)
#             else:
#                 cur = 0
#         return ans

# class Solution:
#     def goodIndices(self, A: List[int], k: int) -> List[int]:
#         n = len(A)
        
#         prefix = [0] * (n + 1) 
#         last = 10000005
#         for i in range(n):
#             if A[i] <= last:
#                 prefix[i + 1] = prefix[i] + 1
#             else:
#                 prefix[i + 1] = 1
#             last = A[i]

#         suffix = [0] * (n + 1)
#         last = 0
#         for i in range(n - 1, 0, -1):
#             if A[i] <= last:
#                 suffix[i - 1] = suffix[i] + 1
#             else:
#                 suffix[i -1] = 1
#             last = A[i]
        
#         ans = []
#         for i in range(1, n):
#             if prefix[i] >= k and suffix[i] >= k:
#                 ans.append(i)
        
#         return ans

# A = [2,1,1,1,3,4,1]
# k = 2
# s = Solution()

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        ans = 0
        n = len(vals)
        C = collections.Counter(vals)

        nxt = [[] for _ in range(n)]
        for a, b in edges:
            nxt[a].append(b)
            nxt[b].append(a)

        def dfs(root, pa, val, prefix):
            nonlocal ans
            
            if vals[root] > val:
                for ch in nxt[root]:
                    if ch == pa:
                        continue
                    dfs(ch, root, val, 0)
                return 0
            elif vals[root] < val:
                ch_ans = []
                for ch in nxt[root]:
                    if ch == pa:
                        continue
                    rt = dfs(ch, root, val, prefix)
                    ch_ans.append(rt)
                ret = sum(ch_ans)
                n = len(ch_ans)
                cur_ans = 0
                for i in range(n - 1):
                    for j in range(i + 1, n):
                        cur_ans += ch_ans[i] * ch_ans[j]
                ans += cur_ans
                return ret 
            else:  # vals[root] == val
                ch_ans = []
                for ch in nxt[root]:
                    if ch == pa:
                        continue
                    rt = dfs(ch, root, val, prefix + 1)
                    ch_ans.append(rt)
                ret = sum(ch_ans) + 1
                
                n = len(ch_ans)
                cur_ans = 0
                for i in range(n - 1):
                    for j in range(i + 1, n):
                        cur_ans += ch_ans[i] * ch_ans[j]
                ans += cur_ans + prefix
                return ret 

        for k, v in C.items():
            print(k, v)
            if v == 1:
                ans += 1
            else:
                dfs(0, -1, v, 0)
            
        return ans

vals = [1,3,2,1,3]
edges = [[0,1],[0,2],[2,3],[2,4]]
s = Solution()
print(s.numberOfGoodPaths(vals, edges))






























