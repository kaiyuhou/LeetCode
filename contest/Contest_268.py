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
#     def maxDistance(self, colors: List[int]) -> int:
#         ans = 0
#         n = len(colors)
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 if colors[i] != colors[j]:
#                     ans = max(ans, j - i)
#         return ans


# class Solution:
#     def wateringPlants(self, plants: List[int], capacity: int) -> int:
#         cur = capacity
#         ans = 0
#         for i, p in enumerate(plants):
#             if cur >= p:
#                 ans += 1
#                 cur -= p
#             else:
#                 ans += i * 2 + 1
#                 cur = capacity - p
#         return ans


# import bisect
# class RangeFreqQuery:
#
#     def __init__(self, arr: List[int]):
#         self.dp = {}
#         for i, a in enumerate(arr):
#             if a not in self.dp:
#                 self.dp[a] = [i]
#             else:
#                 self.dp[a].append(i)
#
#     def query(self, left: int, right: int, value: int) -> int:
#         if value not in self.dp:
#             return 0
#
#         left_index = bisect.bisect_left(self.dp[value], left)
#         right_index = bisect.bisect_right(self.dp[value], right)
#         return right_index - left_index

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_mirror(a):
            a = str(int(a, k))
            return a == a[::-1]

        # def to_base(a, base):
        #     digits = 0
        #     while a:
        #         digits = digits * 10 + (a % base)
        #         # print(digits)
        #         a //= base
        #     return digits
        #
        # ans = 0
        # cur = 1
        # while n > 0:
        #     if cur % 10 == 0 or cur % k == 0:
        #         cur += 1
        #         continue
        #
        #     if is_mirror(str(cur)) and is_mirror(str(to_base(cur, k))):
        #         print(cur, to_base(cur, k))
        #         ans += cur
        #         n -= 1
        #     cur += 1

        if n < k:
            return (1 + n) * n // 2

        ans = 0
        odd_arr = [str(i) for i in range(k)]
        even_arr = [str(i) + str(i) for i in range(k)]
        arr = [odd_arr, even_arr]
        # print(arr)

        for index in (0, 1):
            for num in arr[index]:
                # print(num)

                if num[0] == '0':
                    continue

                if is_mirror(num):
                    n -= 1
                    ans += int(num, k)
                    # print(num, int(num, k))

                if n == 0:
                    break
            if n == 0:
                break

        while n > 0:
            cur = [[],[]]
            for index in (0, 1):
                for i in range(k):
                    for num in arr[index]:
                        cur_num = str(i) + num + str(i)
                        cur[index].append(cur_num)
                        if i == 0:
                            continue
                        if is_mirror(cur_num):
                            n -= 1
                            ans += int(cur_num, k)
                            # print(cur_num, int(cur_num, k))

                        if n == 0:
                            break
                    if n == 0:
                        break
                if n == 0:
                    break
            arr = cur
            # print(arr)
        return ans


s = Solution()
k = 7
n = 17
print(s.kMirror(k, n))



















