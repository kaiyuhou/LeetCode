from Tree import *

# class Solution:
#     def calculateTime(self, keyboard: str, word: str) -> int:
#         ans = 0
#         pos = 0
#         dp = {}
#         for i, c in enumerate(keyboard):
#             dp[c] = i
#
#         for c in word:
#             ans += abs(dp[c] - pos)
#             pos = dp[c]
#
#         return ans
#
#
#
# s = Solution()
# keyboard = "abcdefghijklmnopqrstuvwxyz"
# word = "cba"
# keyboard = "pqrstuvwxyzabcdefghijklmno"
# word = "leetcode"
# print(s.calculateTime(keyboard, word))


# class FileSystem:
#     def __init__(self):
#         self.dp = {}
#         self.dp[''] = -1
#
#     def create(self, path: str, value: int) -> bool:
#         if path in self.dp.keys():
#             return False
#
#         k = path.rindex('/')
#         if path[:k] not in self.dp.keys():
#             return False
#
#         self.dp[path] = value
#         return True
#
#     def get(self, path: str) -> int:
#         if path not in self.dp.keys():
#             return -1
#         return self.dp[path]
#
# s = FileSystem()
# print(s.create("/leet", 1))
#
# print(s.create("/leet/code", 2))
# print(s.get("/leet/code"))
#
# print(s.create("/c/d", 1))
# print(s.get("/c"))
#

from heapq import *
class Solution:
    def minCostToSupplyWater(self, N: int, wells, pipes) -> int:
        neg = [[] for _ in range(N)]
        f = [i for i in range(N)]
        # dp = [-1 for i in range(N)]

        def find(a):
            while f[a] != a:
                a = f[a]
            return a


        for i, j, c in pipes:
            i = i - 1
            j = j - 1
            neg[i].append((j, c))
            neg[j].append((i, c))
            f[i] = find(j)

        for i in range(N):
            f[i] = find(i)

        G = {}
        for i in range(N):
            if f[i] not in G.keys():
                G[f[i]] = [i]
            else:
                G[f[i]].append(i)

        ans = 0
        def get_ans(A):
            if len(A) == 0:
                return 0
            if len(A) == 1:
                return wells[A[0]]


            left_well = []
            small_i = A[0]
            for i in A:
                left_well.append(wells[i])
                if wells[i] < wells[small_i]:
                    small_i = i

            ans = 0
            solved = set()
            ans += wells[small_i]
            left_well.remove(wells[small_i])
            solved.add(small_i)
            edges = []
            heapify(edges)
            for n, c in neg[small_i]:
                heappush(edges, (c, n))

            for i in range(len(A) - 1):
                c, cur = heappop(edges)
                while cur in solved:
                    c, cur = heappop(edges)

                if c > min(left_well):
                    all_well = set(A)
                    left = all_well - solved
                    ans += get_ans(list(left))
                    return ans

                ans += c
                solved.add(cur)
                left_well.remove(wells[cur])
                for n, c in neg[cur]:
                    heappush(edges, (c, n))

            return ans

        for k, A in G.items():
            ans += get_ans(A)

        return ans

s = Solution()
n = 4
wells = [1,2,2, 100]
pipes = [[1,2,1],[2,3,1]]

n = 5
wells = [46012,72474,64965,751,33304]
pipes = [[2,1,6719],[3,2,75312],[5,3,44918]]

print(s.minCostToSupplyWater(n, wells, pipes))
#
# from heapq import *
# class Solution:
#     def connectSticks(self, sticks) -> int:
#         A = sorted(sticks)
#         heapify(A)
#         ans = 0
#         while len(A) > 1:
#             sum = heappop(A) + heappop(A)
#             heappush(A, sum)
#             ans += sum
#
#         return ans
#
# s = Solution()
# A = [2,4,3]
# A = [1,8,3,5]
# print(s.connectSticks(A))






