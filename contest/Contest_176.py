from types import *
from Tree import *

# class Solution:
#     def countNegatives(self, grid) -> int:
#         ans = 0
#         for r in grid:
#             for i in r:
#                 if i < 0:
#                     ans += 1
#         return ans
#
# grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# s = Solution()
# print(s.countNegatives(grid))


# class ProductOfNumbers:
#
#     def __init__(self):
#         self.dp = [0]
#         self.arr = []
#
#     def add(self, num: int) -> None:
#         if num == 0:
#             self.arr.append(len(self.dp) - 1)
#         if self.dp[-1] == 0:
#             self.dp.append(num)
#         else:
#             self.dp.append(self.dp[-1] * num)
#
#     def getProduct(self, k: int) -> int:
#         # print(self.arr)
#         N = len(self.dp) - 2
#         K = N - k + 1
#         if len(self.arr) > 0 and K <= self.arr[-1]:
#             return 0
#         if 0 == self.dp[-1-k]:
#             return self.dp[-1]
#         return self.dp[-1] // self.dp[-1 - k]
#
# p = ProductOfNumbers()
# p.add(3)
# p.add(0)
# p.add(2)
# p.add(5)
# p.add(4)
# print(p.getProduct(2))
# print(p.getProduct(3))

# import heapq
# class Solution:
#     def maxEvents(self, events) -> int:
#         end = 1
#         E = []
#         N = len(events)
#         for s, e in events:
#             E.append((s, e))
#             end = max(e, end)
#         E.sort()
#         start = E[0][0]
#         H = []
#
#         ans = 0
#         j = 0
#         for i in range(start, end + 1):
#             while j < N and E[j][0] == i:
#                 heapq.heappush(H, E[j][1])
#                 j += 1
#
#             if len(H) == 0:
#                 continue
#             now = heapq.heappop(H)
#             while len(H) > 0 and now < i:
#                 now = heapq.heappop(H)
#             if now >= i:
#                 ans += 1
#         return ans
#
# s = Solution()
# events = [[1,2],[2,3],[3,4]]
# events= [[1,2],[2,3],[3,4],[1,2]]
# events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
# events = [[1,100000]]
# events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
# # events = [[1,10],[2,2],[2,2],[2,2],[2,2]]
# print(s.maxEvents(events))


import heapq
class Solution:
    def isPossible(self, target) -> bool:
        N = len(target)
        S = sum(target)
        A = [-a for a in target]
        heapq.heapify(A)

        while len(A) > 0:
            now = -heapq.heappop(A)
            if now == 1:
                return True
            rest = S - now
            # print(now, rest)
            now = now - rest
            S -= rest
            if now > rest:
                T = now // rest
                now -= T * rest
                S -= T * rest
            if now < 1:
                return False
            heapq.heappush(A, -now)
        return True

s = Solution()
target = [9,3,5]
# target = [1,1,1,2]
# target = [30,1,1,69,1,11]
# target = [1,1,85,13,43,1,1]
target = [8,5]
print(s.isPossible(target))













