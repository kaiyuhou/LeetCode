from typing import *
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
#     def sortEvenOdd(self, nums: List[int]) -> List[int]:
#         A = nums[0::2]
#         A.sort()
#         B = nums[1::2]
#         B.sort(reverse=True)
#         ans = [0] * len(nums)
#         for i in range(len(nums)):
#             ans[i] = A[i // 2] if i % 2 == 0 else B[i // 2]
#         return ans
#
# s = Solution()
# nums = [4,1,2,3]
# print(s.sortEvenOdd(nums))

# class Solution:
#     def smallestNumber(self, num: int) -> int:
#         S = list(str(num))
#         if num < 0:
#             S = S[1:]
#             S.sort(reverse=True)
#             return int('-' + ''.join(S))
#         elif num == 0:
#             return 0
#         else:
#             S.sort()
#             if S[0] == '0':
#                 i = 0
#                 while S[i] == '0':
#                     i += 1
#                 S[0] = S[i]
#                 S[i] = '0'
#             return int(''.join(S))
#
# s = Solution()
# num = 31000
# print(s.smallestNumber(num))

# class Bitset:
#
#     def __init__(self, size: int):
#         self.A = [0] * size
#         self.flag = 0
#         self.cnt = 0
#         self.n = size
#
#     def fix(self, idx: int) -> None:
#         if self.flag ^ self.A[idx] == 0:
#             self.A[idx] = self.flag ^ 1
#             self.cnt += 1
#
#     def unfix(self, idx: int) -> None:
#         if self.flag ^ self.A[idx] == 1:
#             self.A[idx] = self.flag ^ 0
#             self.cnt -= 1
#
#     def flip(self) -> None:
#         self.flag = self.flag ^ 1
#         self.cnt = self.n - self.cnt
#
#     def all(self) -> bool:
#         return self.cnt == self.n
#
#     def one(self) -> bool:
#         return self.cnt > 0
#
#     def count(self) -> int:
#         return self.cnt
#
#     def toString(self) -> str:
#         return ''.join([str(self.flag ^ a)  for a in self.A])


class Solution:
    def minimumTime(self, s: str) -> int:
        ans = 0

        i = 0
        while i < len(s) and s[i] == '1':
            i += 1
        ans += i

        s = s[i:]
        s = s[::-1]

        i = 0
        while i < len(s) and s[i] == '1':
            i += 1
        ans += i
        s = s[i:]

        if not s:
            return ans

        dp_l = {}
        dp_r = {}
        n = len(s)

        # print(s)
        # print(ans)

        dp_l[-1, 0] = 0  # remove self edge
        dp_l[-1, 1] = 0  # remove from middle
        last_1 = -1
        for i in range(n):
            if s[i] == '0':
                dp_l[i, 0] = dp_l[i - 1, 0] + 1
                dp_l[i, 1] = dp_l[i - 1, 1]
            else:
                dp_l[i, 0] = dp_l[i - 1, 0] + 1
                dp_l[i, 1] = min(dp_l[last_1, 0], dp_l[last_1, 1]) + 2
                last_1 = i

        # print(dp_l)

        dp_r[n, 0] = 0
        dp_r[n, 1] = 0
        last_1 = n
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp_r[i, 0] = dp_r[i + 1, 0] + 1
                dp_r[i, 1] = dp_r[i + 1, 1]
            else:
                dp_r[i, 0] = dp_r[i + 1, 0] + 1
                dp_r[i, 1] = min(dp_r[last_1, 0], dp_r[last_1, 1]) + 2
                last_1 = i

        cur_ans = len(s)

        # print(dp_r)
        #
        # print(len(s))

        idxs = [-1]
        for i in range(n):
            if s[i] == '1':
                idxs.append(i)
        idxs.append(n)

        # print(idxs)

        for i in range(len(idxs) - 1):
            min_ans = min(dp_l[idxs[i], 0], dp_l[idxs[i], 1]) + min(dp_r[idxs[i + 1], 0], dp_r[idxs[i + 1], 1])
            cur_ans = min(cur_ans, min_ans)

        return cur_ans + ans


ss = Solution()
s = "1100101"
s = "0010"
s = '0000'
# s = '1111001111'
# s = "010110"
# s = '10011010110011001001110011011010001000110010100110010001111110100101011000101110011111101'
print((ss.minimumTime(s)))
























