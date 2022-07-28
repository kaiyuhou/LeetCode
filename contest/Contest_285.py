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
#     def countHillValley(self, nums: List[int]) -> int:
#         A = [nums[0]]
#         n = len(nums)
#         for i in range(1, n):
#             if nums[i] != A[-1]:
#                 A.append(nums[i])
#
#         ans = 0
#         for i in range(1, len(A) - 1):
#             if A[i] > A[i - 1] and A[i] > A[i + 1]:
#                 ans += 1
#             if A[i] < A[i - 1] and A[i] < A[i + 1]:
#                 ans += 1
#         return ans

# class Solution:
#     def countCollisions(self, directions: str) -> int:
#         ans = 0
#         Left = False
#         ToRight = 0
#         for a in directions:
#             if a == 'S':
#                 if ToRight:
#                     ans += ToRight
#                     ToRight = 0
#                 Left = True
#             if a == 'L':
#                 if ToRight:
#                     ans += 1 + ToRight
#                     ToRight = 0
#                     Left = True
#                 elif Left:
#                     ans += 1
#                     Left = True
#             if a == 'R':
#                 ToRight +=1
#         return ans
#
# d = "SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"
# s = Solution()
# print(s.countCollisions(d))


# class Solution:
#     def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
#
#         ans = [0] * 12
#         max_b = 0
#         for i in range(1, 2 ** 12):
#             cur = []
#             for j in range(12):
#                 if i & (1 << j):
#                     cur.append(j)
#             if sum(cur) <= max_b:
#                 continue
#             needs_arr = 0
#             for a in cur:
#                 needs_arr += aliceArrows[a] + 1
#             if needs_arr > numArrows:
#                 continue
#             max_b = sum(cur)
#
#             for idx in range(12):
#                 if idx in cur:
#                     ans[idx] = aliceArrows[idx] + 1
#                 else:
#                     ans[idx] = 0
#             ans[0] += numArrows - needs_arr
#         return ans
#
# s = Solution()
# numArrows = 9
# aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
# print(s.maximumBobPoints(numArrows, aliceArrows))



from typing import Callable, Any


class STNode:
    def __init__(self, l: int, r: int, value: Any = None):
        self.l, self.r = l, r  # 左边界和右边界
        self.value = value  # 节点值(区间值)
        self.left = self.right = self.father = None  # 左右儿子及父指针
        self.lazy = None  # 用于区间和问题的延迟更新标记

    def __repr__(self):
        return f'({self.l}~{self.r}:{self.value})'


class BinIndexTree:
    def __init__(self, data: List, need_build=True):  # 由于建树开销较大，在需要动态建树时将need_build置为False
        self.n = len(data)
        self.c = [0] * (self.n + 1)  # 此时维护的是一个差分数组:data[i] = sum(c[1:i])
        self.cp = [0] * (self.n + 1)  # 差分数组:(1*c[1] + 2*c[2] + ... + n*c[n])
        if need_build:
            self.__build([0] + data)

    def __build(self, data: List):
        for i in range(1, len(data)):  # O(NlogN)
            self.__modify(i - 1, data[i] - data[i - 1])

    def __lowbit(self, x: int):
        return x & (-x)  # => n & (~n + 1), 只留下二进制码中最右侧的1

    def update(self, i: int, value: Any):  # 单点修改: 将某点的值设为value | O(logN)
        self.modify(i, i, value - self.query(i, i))

    def modify(self, i: int, j: int, offset: Any):  # 区间修改: 整个区间的每个值都偏移一个幅度 O(logN)
        self.__modify(i, offset) or self.__modify(j + 1, -offset)

    def query(self, i: int, j: int):  # 区间查询 | O(logN)
        return self.__query(j) - self.__query(i - 1)

    def __query(self, i: int):  # 核心API：求data[0~i]的和(闭区间)
        i += 1  # 统一API
        res = 0
        x = i + 1
        while i > 0:
            res += x * self.c[i] - self.cp[i]  # ☆ 仅能用于求区间合
            i -= self.__lowbit(i)
        return res

    def __modify(self, i: int, diff: Any):  # 核心API：差分修改
        i += 1  # 统一API: 由于树状数组中索引必须从1起，因此对应原数组索引从0起，此处要+1
        d_diff = i * diff
        while i <= self.n:
            self.c[i] += diff
            self.cp[i] += d_diff  # ☆ 仅能用于求区间合
            i += self.__lowbit(i)  # 修改其父级



class Solution:
    def longestRepeating(self, s: str, qC: str, qI: List[int]) -> List[int]:
        A = [1, 2, 3, 4, 3, 2, 1]
        st = BinIndexTree(A)
        print(st.query(0, 3))
        print(st.query(3,6))
        st.modify(1, 4, 2)
        print(st.query(0, 3))
        print(st.query(3, 6))


ss = Solution()
s = "babacc"
queryCharacters = "bcb"
queryIndices = [1,3,3]
print(ss.longestRepeating(s, queryCharacters, queryIndices))























