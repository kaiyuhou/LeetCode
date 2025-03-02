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
#     def countPrefixSuffixPairs(self, A: List[str]) -> int:
#         n = len(A)
#         ans = 0
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 if A[j].startswith(A[i]) and A[j].endswith(A[i]):
#                     ans += 1
#         return ans

# s = Solution()
# A = ["a","aba","ababa","aa"]
# print(s.countPrefixSuffixPairs(A))

# def get_primes():
#     A = [i for i in range(1000000)]
#     B = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}
#     for i in range(101):
#         if i not in B:
#             A[i] = 0

#     for i in range(2, 1000000):
#         if A[i] == 0:
#             continue
#         cur = i + i
#         while cur < 1000000:
#             A[cur] = 0
#             cur += i
#     ans = set()
#     for a in A:
#         if a > 0:
#             ans.add(a)
#     return ans

# import random

# def rabinMiller(num):
#     if num % 2 == 0 or num < 2:
#         return False
#     if num == 3:
#         return True
#     s = num - 1
#     t = 0
#     while s % 2 == 0:
#         s = s // 2
#         t += 1
#     for trials in range(5):
#         a = random.randrange(2, num - 1)
#         v = pow(a, s, num)
#         if v != 1:
#             i = 0
#             while v != (num - 1):
#                 if i == t - 1:
#                     return False
#                 else:
#                     i = i + 1
#                     v = (v ** 2) % num
#     return True


# class Solution:
#     def mostFrequentPrime(self, M: List[List[int]]) -> int:
#         n = len(M)
#         m = len(M[0])
#         C = collections.Counter()
#         nxt = [[0,1], [1,1], [1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

#         def is_valid(x, y):
#             return x >=0 and y >= 0 and x < n and y < m

#         for i in range(n):
#             for j in range(m):
#                 for nx, ny in nxt:
#                     cur = 0
#                     x, y = i, j
#                     while is_valid(x, y):
#                         cur = cur * 10 + M[x][y]
#                         C[cur] += 1
#                         x += nx
#                         y += ny 
#         # P = get_primes()
#         # print(191 in P)

#         ans, ansc = -1, -1
#         # print(C)
#         for a, c in C.most_common():
#             if not rabinMiller(a):
#                 continue
#             if a < 10:
#                 continue
                
#             if ans == -1:
#                 ans = a
#                 ansc = c
#             else:
#                 if ansc == c and ans < a:
#                     ans = a
#                     ansc = c            
#             if c < ansc:
#                 break

#         return ans

# s = Solution()
# # mat = [[1,1],[9,9],[1,1]]
# # mat = [[7]]
# # mat = [[9,7,8],[4,6,5],[2,8,6]]
# mat = [[7],[1]]
# mat = [[7],[9]]
# print(s.mostFrequentPrime(mat))


# class Node:
#      def __init__(self):
#         self.ch = {}

# class Solution:
#     def longestCommonPrefix(self, A: List[int], B: List[int]) -> int:
#         root = Node()
#         for a in A:
#             cur = root
#             for c in str(a):
#                 if c not in cur.ch:
#                     cur.ch[c] = Node()
#                 cur = cur.ch[c]
        
#         ans = 0
#         for b in B:
#             cnt = 0
#             cur = root
#             for c in str(b):
#                 if c not in cur.ch:
#                     break
#                 cnt += 1
#                 cur = cur.ch[c]
#                 ans = max(ans, cnt)
#         return ans

# s = Solution()
# A = [1,10,100]
# B = [1000]
# print(s.longestCommonPrefix(A, B))

def countPrefixSuffixPairs(self, words: List[str]) -> int:
    root = (T := lambda: defaultdict(T))()
    res = 0
    for w in words:
        x = root
        for k in zip(w, reversed(w)):
            res += (x := x[k]).get(0, 0)
        x[0] = x.get(0, 0) + 1
    return res







































