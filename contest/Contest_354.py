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
#     def sumOfSquares(self, nums: List[int]) -> int:
#         ans = 0
#         for i, a in enumerate(nums):
#             if len(nums) % (i + 1) == 0:
#                 ans += a * a
#         return ans

# class Solution:
#     def maximumBeauty(self, A: List[int], k: int) -> int:
#         A.sort()
#         n = len(A)
#         ans = 1
#         j = 0
#         for i in range(n):
#             while j < n and (A[j] - A[i] <= 2 * k):
#                 ans = max(ans, j - i + 1)
#                 j += 1
#         return ans

# class Solution:
#     def minimumIndex(self, A: List[int]) -> int:
#         C = collections.Counter(A)
#         d, f = C.most_common(1)[0]
#         n = len(A)
#         if f * 2 <= n:
#             return -1 
        
#         cur = 0
#         for i, a in enumerate(A):
#             if a == d:
#                 cur += 1
#             if cur * 2 > i + 1 and (f - cur) * 2 > (n - i - 1):
#                 return i
#         return -1

# s = Solution()
# A = [2,1,3,1,1,1,7,1,2,1]
# print(s.minimumIndex(A))

# class Solution:
#     def longestValidSubstring(self, W: str, F: List[str]) -> int:
#         F = set(F)
#         ans = 0
#         right = len(W) - 1
#         for left in range(len(W) - 1, -1, -1):
#             for k in range(left, min(left + 10, right + 1)):
#                 if W[left:k+1] in F:
#                     right = k - 1
#                     break
#             ans = max(ans, right - left + 1)
#         return ans

class Solution:
    def longestValidSubstring(self, W: str, F: List[str]) -> int:
        F = set(F)
        ans = 0
        left = 0
        for right in range(len(W)):
            for k in range(max(left, right - 10), right + 1):
                if W[k:right+1] in F:
                    left = k + 1
            ans = max(ans, right - left + 1)
        return ans



# class Node:
#     def __init__(self, parent):
#         self.child = {}
#         self.valid = {i: True for i in range(26)}
#         self.parent = parent
    
#     def apply(self, c):
#         o = ord(c) - 97
#         if not self.valid[o]:
#             return None
        
#         if o not in self.child:
#             self.child[o] = Node(self)

#         return self.child[o]

#     def set_invalid(self, c):
#         o = ord(c) - 97
#         self.parent.valid[o] = False
    
#     def check(self, s):
#         cur = self
#         for c in s:
#             o = ord(c) - 97
#             if not cur.valid[o]:
#                 return False
#             if o not in cur.child:
#                 return True
#             cur = cur.child[o]
#         return True    


# class Solution:
#     def longestValidSubstring(self, W: str, F: List[str]) -> int:
#         F = set(F)
#         n = len(W)
#         Flen = [(len(f), f) for f in F]
#         Flen.sort()

#         root = Node(None)

#         for _, f in Flen:
#             # print(f)
            
#             cur = root
#             for c in f:
#                 cur = cur.apply(c)
#                 if cur == None:
#                     break
#             else:
#                 cur.set_invalid(c)
#                 # print(root.check('acb'))

#         i = 0
#         cur = 0
#         ans = 0

#         # print(root.check('acb'))

#         cur_0 = set()

#         while i < n:
#             # print(i, W[i], cur)
#             if i in cur_0:
#                 cur = 0
            
#             ans = max(cur, ans)

#             for j in range(min(10, n - i)):
#                 f = W[i:i+j+1]
#                 if not root.check(f):
#                     cur_0.add(i + j)
#                     break
#             cur += 1
#             i += 1

#         ans = max(cur, ans)
#         return ans 

s = Solution()
word = "tcode"
forbidden = ["de","le","e"]
# word = "acbc"
# forbidden = ["cbc","acb","acb","acbc"]
# word = "aaaabaaacc"
# forbidden = ["bcca","aaa","aabaa","baaac"]
print(s.longestValidSubstring(word, forbidden))


                




















